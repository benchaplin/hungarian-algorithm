'''
    File name: test_graph.py
    Description: Tests for Graph methods.
    Author: Ben Chaplin
    GitHub: https://github.com/benchaplin/hungarian-algorithm
    Package: hungarian_algorithm
    Python Version: 3.7.5
    License: MIT License Copyright (c) 2020 Ben Chaplin
'''

import sys
sys.path.insert(1, '../hungarian_algorithm')
from graph import *
import unittest

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
	'x3': {'y1': 4, 'y3': 1}
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

	def test_is_bipartite_single(self):
		self.assertTrue(Graph({'a': {'b'}}).is_bipartite('a'))

	def test_is_bipartite_pass1(self):
		self.assertTrue(Graph(ex_G).is_bipartite('a'))

	def test_is_bipartite_pass2(self):
		self.assertTrue(Graph(ex_H).is_bipartite('x1'))

	def test_is_bipartite_fail1(self):
		self.assertFalse(Graph(ex_X).is_bipartite('x'))

	def test_is_bipartite_fail2(self):
		self.assertFalse(Graph(ex_Y).is_bipartite('x1'))

	def test_make_complete_bipartite_single(self):
		G = Graph({'a': {'b', 'd'}, 'c': {'d'}})
		G.make_complete_bipartite('a')
		self.assertTrue('b' in G.vertices['c'].neighbors)

	def test_make_complete_bipartite1(self):
		G = Graph(ex_G)
		G.make_complete_bipartite('a')
		self.assertTrue({'b', 'c', 'e'} == G.vertices['a'].neighbors
						and {'b', 'c', 'e'} == G.vertices['d'].neighbors
						and G.vertices['d'].get_edge('c').weight == 0
						and G.vertices['d'].get_edge('e').weight == 0)

	def test_make_complete_bipartite1(self):
		G = Graph(ex_H)
		G.make_complete_bipartite('x1')
		self.assertTrue({'y1', 'y2', 'y3'} == G.vertices['x1'].neighbors
						and {'y1', 'y2', 'y3'} == G.vertices['x2'].neighbors
						and {'y1', 'y2', 'y3'} == G.vertices['x3'].neighbors
						and G.vertices['x1'].get_edge('y3').weight == 0
						and G.vertices['x2'].get_edge('y1').weight == 0
						and G.vertices['x3'].get_edge('y2').weight == 0)

	def test_feasibly_label_single(self):
		G = Graph({'a': {'b'}})
		G.feasibly_label('a')
		self.assertEqual(G.vertices['a'].label, 1)

	def test_feasibly_label1(self):
		G = Graph(ex_G)
		G.feasibly_label('a')
		self.assertEqual(G.vertices['a'].label, 7)

	def test_feasibly_label2(self):
		G = Graph(ex_G)
		G.feasibly_label('d')
		self.assertEqual(G.vertices['d'].label, 5)

	def test_feasibly_label3(self):
		G = Graph(ex_H)
		G.feasibly_label('x1')
		self.assertEqual(G.vertices['x1'].label, 6)

	def test_feasibly_label4(self):
		G = Graph(ex_H)
		G.feasibly_label('x2')
		self.assertEqual(G.vertices['x2'].label, 8)

	def test_feasibly_label5(self):
		G = Graph(ex_H)
		G.feasibly_label('x3')
		self.assertEqual(G.vertices['x3'].label, 4)

	def test_generate_feasible_labeling_pass1(self):
		G = Graph(ex_G)
		self.assertTrue(G.generate_feasible_labeling('a'))

	def test_generate_feasible_labeling_pass2(self):
		G = Graph(ex_H)
		self.assertTrue(G.generate_feasible_labeling('x1'))

	def test_generate_feasible_labeling_fail1(self):
		G = Graph(ex_X)
		self.assertFalse(G.generate_feasible_labeling('x'))

	def test_generate_feasible_labeling_fail2(self):
		G = Graph(ex_Y)
		self.assertFalse(G.generate_feasible_labeling('x1'))

	def test_generate_feasible_labeling_single1(self):
		G = Graph({'a': {'b': 1}})
		G.generate_feasible_labeling('a')
		self.assertEqual((G.vertices['a'].label,
						  G.vertices['b'].label),
						 (1, 0))

	def test_generate_feasible_labeling_single2(self):
		G = Graph({'a': {'b': 1}})
		G.generate_feasible_labeling('b')
		self.assertEqual((G.vertices['a'].label,
						  G.vertices['b'].label),
						 (0, 1))

	def test_generate_feasible_labeling1(self):
		G = Graph(ex_G)
		G.generate_feasible_labeling('a')
		self.assertEqual((G.vertices['a'].label, 
						  G.vertices['d'].label,
						  G.vertices['b'].label,
						  G.vertices['c'].label,
						  G.vertices['e'].label), 
						 (7, 5, 0, 0, 0))

	def test_generate_feasible_labeling2(self):
		G = Graph(ex_H)
		G.generate_feasible_labeling('x1')
		self.assertEqual((G.vertices['x1'].label, 
						  G.vertices['x2'].label, 
						  G.vertices['x3'].label,
						  G.vertices['y1'].label,
						  G.vertices['y2'].label,
						  G.vertices['y3'].label), 
						 (6, 8, 4, 0, 0, 0))

	def test_edge_in_equality_subgraph_single(self):
		G = Graph({'a': {'b': 1}})
		G.generate_feasible_labeling('a')
		e = G.vertices['a'].get_edge('b')
		self.assertTrue(G.edge_in_equality_subgraph(e))

	def test_edge_in_equality_subgraph_pass1(self):
		G = Graph(ex_G)
		G.generate_feasible_labeling('a')
		e = G.vertices['a'].get_edge('c')
		self.assertTrue(G.edge_in_equality_subgraph(e))

	def test_edge_in_equality_subgraph_pass2(self):
		G = Graph(ex_H)
		G.generate_feasible_labeling('x1')
		e = G.vertices['x1'].get_edge('y2')
		self.assertTrue(G.edge_in_equality_subgraph(e))

	def test_edge_in_equality_subgraph_fail1(self):
		G = Graph(ex_G)
		G.generate_feasible_labeling('a')
		e = G.vertices['a'].get_edge('e')
		self.assertFalse(G.edge_in_equality_subgraph(e))

	def test_edge_in_equality_subgraph_fail2(self):
		G = Graph(ex_H)
		G.generate_feasible_labeling('x1')
		e = G.vertices['x1'].get_edge('y1')
		self.assertFalse(G.edge_in_equality_subgraph(e))

	def test_equality_subgraph_single(self):
		G = Graph({'a': {'b': 1}})
		G.generate_feasible_labeling('a')
		eq_G = G.equality_subgraph()
		self.assertTrue(eq_G.vertices['a'].get_edge('b'))

	def test_equality_subgraph1(self):
		G = Graph(ex_G)
		G.generate_feasible_labeling('a')
		eq_G = G.equality_subgraph()
		self.assertTrue(eq_G.vertices['a'].get_edge('c')
						and eq_G.vertices['b'].get_edge('d')
						and not eq_G.vertices['a'].get_edge('b')
						and not eq_G.vertices['a'].get_edge('e'))

	def test_equality_subgraph2(self):
		G = Graph(ex_H)
		G.generate_feasible_labeling('x1')
		eq_G = G.equality_subgraph()
		self.assertTrue(eq_G.vertices['x1'].get_edge('y2')
						and eq_G.vertices['x2'].get_edge('y2')
						and eq_G.vertices['x3'].get_edge('y1')
						and not eq_G.vertices['x1'].get_edge('y1')
						and not eq_G.vertices['x2'].get_edge('y3')
						and not eq_G.vertices['x3'].get_edge('y3'))

if __name__ == '__main__':
    unittest.main()
