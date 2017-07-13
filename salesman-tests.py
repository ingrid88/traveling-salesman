import unittest
import salesman
import numpy as np


class Salesman(unittest.TestCase):

    def test_approximate_simple_4_nodes(self):
    	#  A 1 B
      	#  1 2 1
    	#  C 1 D
    	matrix = np.array([[np.nan,1,1,2],[1,np.nan,2,1],[1,2,np.nan,1],[2,1,1,np.nan]])
        min_path, min_distance = salesman.compute_approximate_path(matrix, 0)
        print min_path
        self.assertEqual(min_distance,4)

    def test_approximate_simple_4_nodes_starts_2(self):
    	#  A 1 B
      	#  1 2 1
    	#  C 1 D
    	matrix = np.array([[np.nan,1,1,2],[1,np.nan,2,1],[1,2,np.nan,1],[2,1,1,np.nan]])
        min_path, min_distance = salesman.compute_approximate_path(matrix, 2)
        print min_path
        self.assertEqual(min_distance,4)

    def test_approximate_simple_4_nodes_2(self):
    	#  A 2 B
      	#  2 1 2
    	#  C 2 D
    	matrix = np.array([[np.nan,2,2,1],[2,np.nan,1,2],[2,1,np.nan,2],[1,2,2,np.nan]])
        min_path, min_distance = salesman.compute_approximate_path(matrix, 0)
        print min_path
        self.assertEqual(min_distance,6)

    def test_brute_simple_4_nodes(self):
    	#  A 1 B
      	#  1 2 1
    	#  C 1 D
    	matrix = np.array([[np.nan,1,1,2],[1,np.nan,2,1],[1,2,np.nan,1],[2,1,1,np.nan]])
        min_path, min_distance = salesman.compute_brute_path(matrix, 0)
        print min_path
        self.assertEqual(min_distance,4)

    def test_brute_simple_4_nodes_starts_2(self):
    	#  A 1 B
      	#  1 2 1
    	#  C 1 D
    	matrix = np.array([[np.nan,1,1,2],[1,np.nan,2,1],[1,2,np.nan,1],[2,1,1,np.nan]])
        min_path, min_distance = salesman.compute_brute_path(matrix, 2)
        print min_path
        self.assertEqual(min_distance,4)

    def test_brute_simple_4_nodes_2(self):
    	#  A 2 B
      	#  2 1 2
    	#  C 2 D
    	matrix = np.array([[np.nan,2,2,1],[2,np.nan,1,2],[2,1,np.nan,2],[1,2,2,np.nan]])
        min_path, min_distance = salesman.compute_brute_path(matrix, 0)
        print min_path
        self.assertEqual(min_distance,6)

    def test_brute_simple_ordered(self):
    	#  A 1 B
      	#  1 2 1
    	#  C 1 D
    	matrix = np.array([[np.nan,1,1,2],[1,np.nan,2,1],[1,2,np.nan,1],[2,1,1,np.nan]])
        min_path, min_distance = salesman.compute_brute_path_ordered(matrix, [(0,3),(2,1)])
        print min_path
        self.assertEqual(min_distance,3)
        self.assertEqual(min_path,[0,2,3,1])

if __name__ == '__main__':
    unittest.main()
