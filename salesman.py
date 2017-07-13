from haversine import haversine
import numpy as np
import itertools
import webbrowser
import pdb
# christofedis
# Data from : http://www.uscampgrounds.info/takeit.html
az_campgrounds = {
    'Agave Gulch Military': (-110.861, 32.18),
    'Alamo Lake State Park': (-113.579, 34.231),
    'Alpine Divide': (-109.153, 33.895),
    'Alto Pit': (-112.561, 34.589),
    # 'Apache Flats Military -  Fort Huachuca': (-110.366, 31.56),
    # 'Arcadia': (-109.819, 32.649),
    # 'Ashurst Lake': (-111.409, 35.018),
    # 'Aspen': (-110.946, 34.327),
    # 'Aspen': (-109.314, 33.807),
    # 'Bachelors Cove': (-111.204, 33.714),
    # 'Bartlett Flat': (-111.639, 33.84),
    # 'Bathtub': (-109.307, 31.781),
    # 'Beaver Creek': (-111.714, 34.67),
    # 'Benny Creek': (-109.449, 34.044),
    'Bermuda Flat': (-111.226, 33.746)
    # 'Black Canyon Rim': (-110.743, 34.305),
    # 'Black Jack': (-109.08, 33.057),
    # 'Blue Ridge': (-111.201, 34.591)
}


def campground_distances(az_campgrounds):
    l = len(az_campgrounds.keys())
    d = np.zeros((l, l))
    for i in range(l):
        for j in range(l):
            if i == j:
                d[i, j] = np.nan
            else:
                d[i, j] = haversine(
                    az_campgrounds[az_campgrounds.keys()[i]],
                    az_campgrounds[az_campgrounds.keys()[j]])

    return d


def all_orders_of_places(matrix):
    # l = len(places)
    # pdb.set_trace()
    # orders = perms(l, l)
    # values = range(len(places))
    # d = dict(zip(values, places))
    # return [[d[x] for x in order] for order in orders]
    m_shape = len(matrix)
    return itertools.permutations(range(m_shape), m_shape)

# storage = []
def perms(n, m, ls=[]):
    if m == 0:
        print ls
        return
    for i in range(0, n):
        if i not in ls:
            perms(n, m-1, ls+[i])
        else:
            continue


def approximate_distance(start, matrix):
    # choose the closest of all places
    min_path = [start]
    location = start
    matrix_copy = np.copy(matrix)
    min_distance = 0
    for i in range(len(matrix))[0:-1]:
        # pdb.set_trace()
        row = matrix_copy[location][range(len(matrix))]
        previous_location = location
        # 1. for every available distance, choose the shortest one
        location = np.nanargmin(row)
        # 2. remove the used connection index 
        for j in range(len(matrix)):
            matrix_copy[j][previous_location] = np.nan
        # 3. append location to path
        min_path.append(location)
        min_distance += matrix[previous_location][location]
    min_path.append(start)
    min_distance += matrix[location][start]

    return [min_path, min_distance]


def compute_distance(path, matrix):
    values = range(len(matrix))
    min_distance = 0
    for i, location in enumerate(path[0:-1]):
        min_distance += matrix[path[i]][path[i+1]]
    return min_distance


def compute_approximate_path(matrix, start):
    min_path, min_distance = approximate_distance(start, matrix)
    return [min_path, min_distance]


def compute_brute_path(matrix, start):
    # pdb.set_trace()
    # compute all possible paths
    paths = all_orders_of_places(matrix)

    # get all paths that start with start
    paths = [path for path in paths if path[0] == start]
    # pdb.set_trace()     
    min_distance = 100000
    min_path = []

    for i, path in enumerate(paths):
        path = path + (path[0],)
        computed_distance = compute_distance(path, matrix)
        # print computed_distance
        if min_distance > computed_distance:
            min_path = path
            min_distance = computed_distance

    return [min_path, min_distance]


def show_path(min_path):
    # Open URL in a new tab, if a browser window is already open.
    url = 'https://www.google.com/maps/dir/'
    # pdb.set_trace()
    for loc in min_path:
        url += str(az_campgrounds[az_campgrounds.keys()[loc]][1]) + "," \
            + str(az_campgrounds[az_campgrounds.keys()[loc]][0]) + "/"
    webbrowser.open_new_tab(url)

# min_path, min_distance = compute_brute_path()
# start = 0
# matrix = campground_distances(az_campgrounds)
# min_path, min_distance = compute_approximate_path(matrix, start)
# print "solution"
# print min_path
# print min_distance
# show_path(min_path)
