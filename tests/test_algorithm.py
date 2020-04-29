'''
    File name: test_algorithm.py
    Description: Tests for Hungarian Algorithm.
    Author: Ben Chaplin
    GitHub: https://github.com/benchaplin/hungarian-algorithm
    Package: hungarian_algorithm
    Python Version: 3.7.5
    License: MIT License Copyright (c) 2020 Ben Chaplin
'''

import sys
sys.path.insert(1, '../hungarian_algorithm')
from algorithm import find_matching
import unittest

ex_G = {
	'a': {'b': 2, 'c': 7, 'e': 1},
	'd': {'b': 5}
}

exp_matching_G = {
	(('a', 'c'), 7), 
	(('d', 'b'), 5)
}

ex_H = {
	'x1': {'y1': 1, 'y2': 6},
	'x2': {'y2': 8, 'y3': 6},
	'x3': {'y1': 4, 'y3': 1}
}

exp_matching_H = {
	(('x1', 'y2'), 6), 
	(('x2', 'y3'), 6), 
	(('x3', 'y1'), 4)
}

ex_J = {
	'x1': {'y1': 6, 'y2': 1, 'y5': 3},
	'x2': {'y1': 8, 'y2': 7, 'y5': 5},
	'x3': {'y2': 9, 'y3': 2},
	'x4': {'y2': 10, 'y3': 1, 'y4': 8, 'y5': 6},
	'x5': {'y4': 7, 'y5': 3}
}

exp_matching_J = {
	(('x2', 'y5'), 5), 
	(('x1', 'y1'), 6), 
	(('x3', 'y3'), 2), 
	(('x4', 'y2'), 10), 
	(('x5', 'y4'), 7)
}

ex_K = {
	'x1': {'y1': 4, 'y3': 2},
	'x2': {'y1': 3, 'y2': 1},
	'x3': {'y2': 6, 'y3': 2}
}

exp_matching_K = {
	(('x2', 'y1'), 3), 
	(('x3', 'y2'), 6), 
	(('x1', 'y3'), 2)
}

ex_L = {
	'Ann': {'RB': 3, 'CAM': 2, 'GK': 1},
	'Ben': {'LW': 3, 'S': 2, 'CM': 1},
	'Cal': {'CAM': 3, 'RW': 2, 'SWP': 1},
	'Dan': {'S': 3, 'LW': 2, 'GK': 1},
	'Ela': {'GK': 3, 'LW': 2, 'F': 1},
	'Fae': {'CM': 3, 'GK': 2, 'CAM': 1},
	'Gio': {'GK': 3, 'CM': 2, 'S': 1},
	'Hol': {'CAM': 3, 'F': 2, 'SWP': 1},
	'Ian': {'S': 3, 'RW': 2, 'RB': 1},
	'Jon': {'F': 3, 'LW': 2, 'CB': 1},
	'Kay': {'GK': 3, 'RW': 2, 'LW': 1, 'LB': 0}
}

exp_matching_L = {
	(('Cal', 'CAM'), 3), 
	(('Jon', 'F'), 3), 
	(('Fae', 'CM'), 3), 
	(('Hol', 'SWP'), 1), 
	(('Dan', 'CB'), 0), 
	(('Ann', 'RB'), 3),
	(('Gio', 'LB'), 0), 
	(('Ian', 'S'), 3), 
	(('Ela', 'GK'), 3), 
	(('Ben', 'LW'), 3), 
	(('Kay', 'RW'), 2)
}

class TestGraphMethods(unittest.TestCase):

	def test_hungarian_algorithm1(self):
		self.assertEqual(set(find_matching(ex_G)), exp_matching_G)

	def test_hungarian_algorithm1_total(self):
		self.assertEqual(find_matching(ex_G, "total"), 12)

	def test_hungarian_algorithm2(self):
		self.assertEqual(set(find_matching(ex_H)), exp_matching_H)

	def test_hungarian_algorithm2_total(self):
		self.assertEqual(find_matching(ex_H, "total"), 16)

	def test_hungarian_algorithm3(self):
		self.assertEqual(set(find_matching(ex_J)), exp_matching_J)

	def test_hungarian_algorithm3_total(self):
		self.assertEqual(find_matching(ex_J, "total"), 30)

	def test_hungarian_algorithm4(self):
		self.assertEqual(set(find_matching(ex_K)), exp_matching_K)

	def test_hungarian_algorithm4_total(self):
		self.assertEqual(find_matching(ex_K, "total"), 11)

	def test_hungarian_algorithm5(self):
		self.assertEqual(set(find_matching(ex_L)), exp_matching_L)

	def test_hungarian_algorithm5_total(self):
		self.assertEqual(find_matching(ex_L, "total"), 24)

if __name__ == '__main__':
    unittest.main()
