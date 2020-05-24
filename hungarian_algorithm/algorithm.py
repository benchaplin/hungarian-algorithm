'''
    File name: algorithm.py
    Description: The Hungarian Method for the assignment problem.
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

	def __init__(self, G = {}, negate = False):
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
					self.add_edge(v1, v2, G[v1][v2], negate)
				else:
					self.add_edge(v1, v2)

	def add_vertex(self, key):
		'''Add a vertex to the graph.

		Parameters
		----------
		key : str, required
		'''
		self.vertices[key] = Vertex(key)

	def add_edge(self, v1, v2, weight = 1, negate = False):
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

		if negate:
			e = Edge(v1, v2, -weight)
		else:
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
		max = None

		for e in self.vertices[v].indicent_edges:
			if max is None or e.weight > max:
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


def generate_feasible_labeling(G, start_vertex):
	'''Generate the initial feasible labeling.

	Parameters
	----------
	G : Graph, required
	start_vertex : str, required (any vertex key)

	Return
	----------
	bool (True if bipartite and labeling generated,
		  False if not bipartite and labeling)
	'''

	if start_vertex == None:
		return True

	G.feasibly_label(start_vertex)
	queue = []
	queue.append(start_vertex)

	while queue:
		v = queue.pop()

		for w in G.vertices[v].neighbors:
			if G.vertices[w].label == None:
				if G.vertices[v].label == 0:
					G.feasibly_label(w)
				else:
					G.vertices[w].set_label(0)
				queue.append(w)
			elif G.vertices[w].label == G.vertices[v].label:
				return False

	return True

def vertex_saturated(v, M):
	'''Determine whether a vertex is saturated by a matching.

	Parameters
	----------
	v : str (vertex key)
	M : {Edge} (set of edges)

	Return
	----------
	str / bool (relevant neighbor if saturated, False if unsaturated)
	'''
	for e in M:
		if v == e.vertices[0]:
			return e.vertices[1]
		elif v == e.vertices[1]:
			return e.vertices[0]	

	return False

def find_matching(_G, matching_type = 'max', return_type = 'list'):
	'''Find maximum/minimum-weighted matching.

	Parameters
	----------
	_G : dict, required (valid Graph dict)

	Return
	----------
	[(str, int)] (list of edges in matching described as:
				  a tuple ('x-y', weight))
		or
	int (total weight)
	'''
	# Step 1
	# Create a bipartite graph, make it complete
	negate = False if matching_type == 'max' else True
	G = Graph(_G, negate)
	start_vertex = list(G.vertices.keys())[0]
	G.make_complete_bipartite(start_vertex)

	# Generate an initial feasible labeling
	is_bipartite = G.generate_feasible_labeling(start_vertex)

	if not is_bipartite:
		return False

	# Create the equality subgraph
	eq_G = G.equality_subgraph()

	# Create an initial matching
	M = set()

	for x in eq_G.vertices:
		if eq_G.vertices[x].in_left and not vertex_saturated(x, M):
			max_edge = None
			for y in eq_G.vertices[x].neighbors:
				if not vertex_saturated(y, M):
					if max_edge is None or eq_G.vertices[x].get_edge(y).weight > max_edge.weight:
						max_edge = eq_G.vertices[x].get_edge(y)
			if max_edge is not None:
				M.add(max_edge)

	S = set()
	T = set()
	path_end = None

	while len(M) < int(len(eq_G.vertices)/2):
		if path_end is None:
			# Step 2
			# Add new augmenting tree
			for x in eq_G.vertices:
				if eq_G.vertices[x].in_left and not vertex_saturated(x, M):
					S.add(x)
					path_end = x
					break
		
		# Calculate neighbors of S
		S_nbs = set()
		for v in S:
			S_nbs = S_nbs | eq_G.vertices[v].neighbors

		if S_nbs == T:
			# Step 3
			alpha = None
			for x in S:
				for y in G.vertices.keys() - T:
					if not G.vertices[y].in_left and y in G.vertices[x].neighbors:
						new_alpha = G.vertices[x].label + G.vertices[y].label - G.vertices[x].get_edge(y).weight
						alpha = new_alpha if alpha is None or new_alpha < alpha else alpha
			
			if alpha != None:
				# Update the labeling
				for u in S:
					G.vertices[u].label = G.vertices[u].label - alpha
				for v in T:
					G.vertices[v].label = G.vertices[v].label + alpha

				# Update the equality subgraph
				eq_G = G.equality_subgraph()

		# Calculate neighbors of S
		S_nbs = set()
		for v in S:
			S_nbs = S_nbs | eq_G.vertices[v].neighbors

		# Step 4
		if S_nbs != T:
			y = list(S_nbs - T)[0]
			z = vertex_saturated(y, M)

			# Part (i)
			if not z:
				T.add(y)
				
				# Augment the matching
				y_path_last = y
				y_path_curr = y
				matched_nbs = True

				while matched_nbs:
					matched_nbs = False

					for x in S & eq_G.vertices[y_path_curr].neighbors:
						y_matched_nb = vertex_saturated(x, M)
						if y_matched_nb and y_matched_nb != y_path_last:
							matched_nbs = True
							M.add(eq_G.vertices[y_path_curr].get_edge(x))
							M.remove(eq_G.vertices[x].get_edge(y_matched_nb))
							y_path_last = y_path_curr
							y_path_curr = y_matched_nb
							break

					if not matched_nbs:
						M.add(eq_G.vertices[y_path_curr].get_edge(path_end))

				S = set()
				T = set()
				path_end = None

			# Part (ii)
			else:
				# Add to augmenting tree
				S.add(z)
				T.add(y)

	edge_multiple = -1 if matching_type == 'min' else 1;
	if return_type == 'list':
		return list(map(lambda e: ((e.vertices[0], e.vertices[1]), edge_multiple * e.weight), M))
	elif return_type == 'total':
		total = 0
		for e in M:
			total = total + (edge_multiple * e.weight)
		return total
