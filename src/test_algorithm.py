'''
    File name: test_algorithm.py
    Description: Tests for Hungarian Algorithm.
    Author: Ben Chaplin
    GitHub: https://github.com/benchaplin/hungarian-algorithm
    Package: hungarian_algorithm
    Python Version: 3.7.5
    License: MIT License Copyright (c) 2020 Ben Chaplin
'''

import unittest
from algorithm import hungarian_algorithm

ex_G = {
	'a': {'b': 2, 'c': 7, 'e': 1},
	'd': {'b': 5}
}

exp_matching_G = {
	('a-c', 7), 
	('d-b', 5)
}

ex_H = {
	'x1': {'y1': 1, 'y2': 6},
	'x2': {'y2': 8, 'y3': 6},
	'x3': {'y1': 4, 'y3': 1}
}

exp_matching_H = {
	('x1-y2', 6), 
	('x2-y3', 6), 
	('x3-y1', 4)
}

ex_J = {
	'x1': {'y1': 6, 'y2': 1, 'y5': 3},
	'x2': {'y1': 8, 'y2': 7, 'y5': 5},
	'x3': {'y2': 9, 'y3': 2},
	'x4': {'y2': 10, 'y3': 1, 'y4': 8, 'y5': 6},
	'x5': {'y4': 7, 'y5': 3}
}

exp_matching_J = {
	('x2-y5', 5), 
	('x1-y1', 6), 
	('x3-y3', 2), 
	('x4-y2', 10), 
	('x5-y4', 7)
}

ex_K = {
	'x1': {'y1': 4, 'y3': 2},
	'x2': {'y1': 3, 'y2': 1},
	'x3': {'y2': 6, 'y3': 2}
}

exp_matching_K = {
	('x2-y1', 3), 
	('x3-y2', 6), 
	('x1-y3', 2)
}

class TestGraphMethods(unittest.TestCase):

	def test_hungarian_algorithm1(self):
		self.assertEquals(set(hungarian_algorithm(ex_G)), exp_matching_G)

	def test_hungarian_algorithm1_total(self):
		self.assertEquals(hungarian_algorithm(ex_G, "total"), 12)

	def test_hungarian_algorithm2(self):
		self.assertEquals(set(hungarian_algorithm(ex_H)), exp_matching_H)

	def test_hungarian_algorithm2_total(self):
		self.assertEquals(hungarian_algorithm(ex_H, "total"), 16)

	def test_hungarian_algorithm3(self):
		self.assertEquals(set(hungarian_algorithm(ex_J)), exp_matching_J)

	def test_hungarian_algorithm3_total(self):
		self.assertEquals(hungarian_algorithm(ex_J, "total"), 30)

	def test_hungarian_algorithm4(self):
		self.assertEquals(set(hungarian_algorithm(ex_K)), exp_matching_K)

	def test_hungarian_algorithm4_total(self):
		self.assertEquals(hungarian_algorithm(ex_K, "total"), 11)

if __name__ == '__main__':
    unittest.main()
