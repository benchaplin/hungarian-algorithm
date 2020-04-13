'''
    File name: graph.py
    Description: Graph classes to be used in the main algorithm.
    Author: Ben Chaplin
    GitHub: https://github.com/benchaplin/hungarian-algorithm
    Package: hungarian_algorithm
    Python Version: 3.7.5
    License: MIT License Copyright (c) 2020 Ben Chaplin
'''

import copy

class Vertex: 

	def __init__(self, key):
		'''Vertex constructor.

		Parameters
		----------
		key : str, required
		'''
		self.key = key
		self.label = None
		self.neighbors = set()
		self.indicent_edges = set()
		self.in_left = None

	def get_edge(self, neighbor):
		'''Get indicent edge.

		Parameters
		----------
		neighbor : str, required (vertex key)

		Return
		----------
		Edge (or False if doesn't exist)
		'''
		for e in self.indicent_edges:
			if neighbor in e.vertices:
				return e

		return False

	def set_label(self, label):
		'''Label the vertex.'''
		self.label = label

	def set_in_left(self, in_left):
		self.in_left = in_left

	def filter_neighbors(self):
		'''Filter neighbors set after update to indicent edges.
		Filter from original set down.
		'''
		new_neighbors = set()

		for v in self.neighbors:
			for e in self.indicent_edges:
				if v == e.vertices[0] or v == e.vertices[1]:
					new_neighbors.add(v)
					break

		self.neighbors = new_neighbors


class Edge:

	def __init__(self, v1, v2, weight = 0):
		'''Edge constructor.

		Parameters
		----------
		v1 : str, required (endpoint1 key)
		v2 : str, required (endpoint2 key)
		weight : int, optional (default = 0)
		'''
		self.vertices = [v1, v2]
		self.weight = weight

	def __eq__(self, e):
		'''Edges with equal endpoints and weights are equal.'''
		return (self.vertices == e.vertices
				and self.weight == e.weight)

	def __hash__(self):
		'''Hash the vertices (frozen set) and weight.'''
		return hash((frozenset(self.vertices), self.weight))


class Graph:

	def __init__(self, G={}):
		'''Graph constructor (for connected graphs).

		Parameters
		----------
		G : dict, optional (default = empty graph)
				key : vertex key
				value : set of neighboring vertices (unweighted graph)
						or 
						dict (weighted graph) 
							key : neighboring vertex key
							value : edge weight
		'''
		self.vertices = {}

		for v1 in G:
			for v2 in G[v1]:
				if type(G[v1]) is dict:
					self.add_edge(v1, v2, G[v1][v2])
				else:
					self.add_edge(v1, v2)

	def add_vertex(self, key):
		'''Add a vertex to the graph.

		Parameters
		----------
		key : str, required
		'''
		self.vertices[key] = Vertex(key)

	def add_edge(self, v1, v2, weight = 1):
		'''Add a vertex to the graph.
		
		Parameters
		----------
		v1 : str, required (endpoint1 key)
		v2 : str, required (endpoint2 key)
		weight : int, optional (default = 1)
		'''
		if v1 not in self.vertices:
			self.add_vertex(v1)
		if v2 not in self.vertices:
			self.add_vertex(v2)

		e = Edge(v1, v2, weight)

		self.vertices[v1].neighbors.add(v2)
		self.vertices[v2].neighbors.add(v1)
		self.vertices[v1].indicent_edges.add(e)
		self.vertices[v2].indicent_edges.add(e)

	def is_bipartite(self, start_vertex):
		'''Determine if graph is bipartite.

		Parameters
		----------
		start_vertex : str, required (any vertex key)
		'''
		if start_vertex == None:
			return True

		self.clear_labeling()
		self.vertices[start_vertex].set_label(1)
		queue = []
		queue.append(start_vertex)

		while queue:
			v = queue.pop()

			for w in self.vertices[v].neighbors:
				if self.vertices[w].label == None:
					self.vertices[w].set_label(1 - self.vertices[v].label)
					queue.append(w)
				elif self.vertices[w].label == self.vertices[v].label:
					return False

		return True

	def make_complete_bipartite(self, start_vertex):
		'''Make bipartite graph complete with weight 0 edges.

		Parameters
		----------
		start_vertex : str, required (any vertex key)
		'''
		if start_vertex == None:
			return True

		self.clear_labeling()
		self.generate_feasible_labeling(start_vertex)

		for x in self.vertices:
			if self.vertices[x].in_left:
				for y in self.vertices:
					if (not self.vertices[y].in_left 
						and y not in self.vertices[x].neighbors):
						self.add_edge(x, y, 0)
		self.clear_labeling()

	def feasibly_label(self, v):
		'''Label a vertex with smallest nonzero feasible label 
		   (= largest indicent edge weight).

		Parameters
		----------
		v : str, required (any vertex key)
		'''
		max = 0

		for e in self.vertices[v].indicent_edges:
			if e.weight > max:
				max = e.weight

		self.vertices[v].set_label(max)
		self.vertices[v].set_in_left(True)

	def generate_feasible_labeling(self, start_vertex):
		'''Generate the initial feasible labeling.

		Parameters
		----------
		start_vertex : str, required (any vertex key)

		Return
		----------
		bool (True if bipartite and labeling generated,
			  False if not bipartite and labeling)
		'''
		if start_vertex == None:
			return True

		self.feasibly_label(start_vertex)
		queue = []
		queue.append(start_vertex)

		while queue:
			v = queue.pop()

			for w in self.vertices[v].neighbors:
				if self.vertices[w].label == None:
					if self.vertices[v].label == 0:
						self.feasibly_label(w)
					else:
						self.vertices[w].set_label(0)
						self.vertices[w].set_in_left(False)
					queue.append(w)
				elif ((self.vertices[w].label == 0 
					   and self.vertices[v].label == 0)
					  or (self.vertices[w].label != 0
					      and self.vertices[v].label != 0)):
					return False

		return True

	def clear_label(self, v):
		'''Reset label to None.'

		Parameters
		----------
		v : str, required (vertex key)
		'''
		self.vertices[v].set_label(None)

	def clear_labeling(self):
		'''Reset all vertices' labels to None.'''
		for v in self.vertices:
			self.vertices[v].set_label(None)

	def edge_in_equality_subgraph(self, e):
		'''Determine whether edge is in equality subgraph
		
		Parameters
		----------
		e : Edge, required

		Return
		----------
		bool (True if in equality subgraph, False if not)
		'''
		e_endpoints = list(e.vertices)
		if (self.vertices[e_endpoints[0]].label == None or 
			self.vertices[e_endpoints[1]].label == None):
			return False
		return e.weight == (self.vertices[e_endpoints[0]].label + 
							self.vertices[e_endpoints[1]].label)

	def equality_subgraph(self):
		'''Create equality subgraph w/ respect to labeling.

		Return
		----------
		Graph (subgraph with all edges e where l(v1) + l(v2) = w(e))
		'''
		eq_H = copy.deepcopy(self)

		for v in eq_H.vertices:
			eq_H.vertices[v].indicent_edges = list(filter(
				self.edge_in_equality_subgraph, 
				eq_H.vertices[v].indicent_edges))
			eq_H.vertices[v].filter_neighbors()

		return eq_H
