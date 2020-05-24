'''
    File name: test_algorithm.py
    Description: Tests for Hungarian Algorithm.
    Author: Ben Chaplin
    GitHub: https://github.com/benchaplin/hungarian-algorithm
    Package: hungarian_algorithm
    Python Version: 3.7.5
    License: MIT License Copyright (c) 2020 Ben Chaplin
'''

from ..algorithm import find_matching
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
	'x1': {'y1': 7, 'y2': 1, 'y5': 3},
	'x2': {'y1': 8, 'y2': 7, 'y5': 5},
	'x3': {'y2': 9, 'y3': 2},
	'x4': {'y2': 10, 'y3': 1, 'y4': 8, 'y5': 6},
	'x5': {'y4': 7, 'y5': 3}
}

exp_matching_J = {
	(('x2', 'y5'), 5), 
	(('x1', 'y1'), 7), 
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

ex_M = {
    'D91': { 'O87': 3668, 'O224': 3880 },
    'D22': { 'O87': 482, 'O224': 1825 }
}

exp_max_matching_M = {
	(('D91', 'O87'), 3668),
	(('D22', 'O224'), 1825)
}

exp_min_matching_M = {
	(('D91', 'O224'), 3880),
	(('D22', 'O87'), 482)
}

ex_N = {
	'A': { '#191': 22, '#122': 14, '#173': 120, '#121': 21, '#128': 4, '#104': 51 },
	'B': { '#191': 19, '#122': 12, '#173': 172, '#121': 21, '#128': 28, '#104': 43 },
	'C': { '#191': 161, '#122': 122, '#173': 2, '#121': 50, '#128': 128, '#104': 39 },
	'D': { '#191': 19, '#122': 22, '#173': 90, '#121': 11, '#128': 28, '#104': 4 },
	'E': { '#191': 1, '#122': 30, '#173': 113, '#121': 14, '#128': 28, '#104': 86 },
	'F': { '#191': 60, '#122': 70, '#173': 170, '#121': 28, '#128': 68, '#104': 104 },
}

exp_min_matching_N = {
	(('A', '#128'), 4),
	(('B', '#122'), 12),
	(('C', '#173'), 2),
	(('D', '#104'), 4),
	(('E', '#191'), 1),
	(('F', '#121'), 28)
}

class TestGraphMethods(unittest.TestCase):

	def test_hungarian_algorithm1(self):
		self.assertEqual(set(find_matching(ex_G)), exp_matching_G)

	def test_hungarian_algorithm1_total(self):
		self.assertEqual(find_matching(ex_G, return_type = 'total'), 12)

	def test_hungarian_algorithm2(self):
		self.assertEqual(set(find_matching(ex_H)), exp_matching_H)

	def test_hungarian_algorithm2_total(self):
		self.assertEqual(find_matching(ex_H, return_type = 'total'), 16)

	def test_hungarian_algorithm3(self):
		self.assertEqual(set(find_matching(ex_J)), exp_matching_J)

	def test_hungarian_algorithm3_total(self):
		self.assertEqual(find_matching(ex_J, return_type = 'total'), 31)

	def test_hungarian_algorithm4(self):
		self.assertEqual(set(find_matching(ex_K)), exp_matching_K)

	def test_hungarian_algorithm4_total(self):
		self.assertEqual(find_matching(ex_K, return_type = 'total'), 11)

	def test_hungarian_algorithm5_total(self):
		self.assertEqual(find_matching(ex_L, return_type = 'total'), 24)

	def test_hungarian_algorithm6_max(self):
		self.assertEqual(set(find_matching(ex_M)), exp_max_matching_M)

	def test_hungarian_algorithm6_min(self):
		self.assertEqual(set(find_matching(ex_M, matching_type = 'min')), exp_min_matching_M)

	def test_hungarian_algorithm6_total_max(self):
		self.assertEqual(find_matching(ex_M, matching_type = 'max', return_type = 'total'), 5493)

	def test_hungarian_algorithm6_total_min(self):
		self.assertEqual(find_matching(ex_M, matching_type = 'min', return_type = 'total'), 4362)

	def test_hungarian_algorithm7_min(self):
		self.assertEqual(set(find_matching(ex_N, matching_type = 'min')), exp_min_matching_N)

	def test_hungarian_algorithm6_total_min(self):
		self.assertEqual(find_matching(ex_N, matching_type = 'min', return_type = 'total'), 51)

if __name__ == '__main__':
    unittest.main()
