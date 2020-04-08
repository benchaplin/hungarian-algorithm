'''
    File name: test.py
    Description: Tests for Graph methods and algorithms.
    Author: Ben Chaplin
    GitHub: https://github.com/benchaplin/hungarian_algorithm
    Package: hungarian_algorithm
    Python Version: 3.7.5
'''


import unittest
from graph import Vertex, Edge, Graph

ex_G = {
	'a': {'b': 2, 'c': 7, 'e': 1},
	'b': {'a': 2, 'd': 5},
	'c': {'a': 7},
	'd': {'b': 5},
	'e': {'a': 1}
}

ex_H = {
	'x1': {'y1': 1, 'y2': 6},
	'x2': {'y2': 8, 'y3': 6},
	'x3': {'y1': 4, 'y3': 6}
}

ex_X = {
	'x': {'y', 'z'},
	'y': {'x', 'z'},
	'z': {'x', 'y'}
}

ex_Y = {
	'x1': {'y1': 1, 'y2': 6},
	'x2': {'y2': 8, 'y3': 6},
	'x3': {'y1': 4, 'y3': 6},
	'y1': {'y2': 2}
}

class TestGraphMethods(unittest.TestCase):

	def test_is_bipartite_empty(self):
		self.assertTrue(Graph({}).is_bipartite(None))

	def test_is_bipartite_pass1(self):
		self.assertTrue(Graph(ex_G).is_bipartite('a'))

	def test_is_bipartite_pass2(self):
		self.assertTrue(Graph(ex_H).is_bipartite('x1'))

	def test_is_bipartite_fail1(self):
		self.assertTrue(Graph(ex_X).is_bipartite('x'))

	def test_is_bipartite_fail2(self):
		self.assertTrue(Graph(ex_Y).is_bipartite('x1'))


if __name__ == '__main__':
    unittest.main()