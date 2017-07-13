import unittest
import salesman
import numpy as np


class Salesman(unittest.TestCase):

    def test_path_nodes_are_unique(self):
    	#  A 1 B
      	#  1 2 1
    	#  C 1 D
    	matrix = np.array([[np.nan,1,2,1],[1,np.nan,2,1],[1,2,np.nan,1],[2,1,1,np.nan]])
        min_path, min_distance = salesman.compute_approximate_path(matrix, 0)
        print min_path
        self.assertEqual(min_distance,4)


if __name__ == '__main__':
    unittest.main()
