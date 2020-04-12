'''
    File name: algorithms.py
    Description: The Hungarian Method for the assignment problem.
    Author: Ben Chaplin
    GitHub: https://github.com/benchaplin/hungarian-algorithm
    Package: hungarian_algorithm
    Python Version: 3.7.5
    License: MIT License Copyright (c) 2020 Ben Chaplin
'''

from graph import Vertex, Edge, Graph
import copy


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

def hungarian_algorithm(_G, return_type = "list"):
	'''Find maximum-weighted matching.

	Parameters
	----------
	_G : dict, required (valid Graph dict)

	Return
	----------
	{Edge} (set of Edges that make up the maximum-weighted matching)
	'''
	G = Graph(_G)
	start_vertex = list(G.vertices.keys())[0]
	G.make_complete_bipartite(start_vertex)

	is_bipartite = G.generate_feasible_labeling(start_vertex)
	if not is_bipartite:
		return False

	eq_G = G.equality_subgraph()
	print('---')
	print('STEP 1')
	print('initial equality subgraph')
	for v in eq_G.vertices:
		print(v, eq_G.vertices[v].label, eq_G.vertices[v].neighbors)

	print('initial matching')
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

	print(list(map(lambda e: e.vertices, M)))
	print('---')

	S = set()
	T = set()
	path_end = None

	while len(M) < int(len(eq_G.vertices)/2):
		if path_end is None:
			print('---')
			print('STEP 2')
			for x in eq_G.vertices:
				if eq_G.vertices[x].in_left and not vertex_saturated(x, M):
					S.add(x)
					print('adding', x, 'to S -> S =', S)
					path_end = x
					break
			print('---')
		
		S_nbs = set()
		for v in S:
			S_nbs = S_nbs | eq_G.vertices[v].neighbors

		if S_nbs == T:
			print('---')
			print('STEP 3')
			print('S = ', S, 'T = ', T)
			print(S_nbs, 'S_nbs', '= T', T)
			alpha = None
			for x in S:
				for y in G.vertices.keys() - T:
					if not G.vertices[y].in_left and y in G.vertices[x].neighbors:
						new_alpha = G.vertices[x].label + G.vertices[y].label - G.vertices[x].get_edge(y).weight
						alpha = new_alpha if alpha is None or new_alpha < alpha else alpha
			print('alpha =', alpha)
			for u in S:
				G.vertices[u].label = G.vertices[u].label - alpha
			for v in T:
				G.vertices[v].label = G.vertices[v].label + alpha
			eq_G = G.equality_subgraph()
			print('New eq subgraph')
			for v in eq_G.vertices:
				print(v, eq_G.vertices[v].label, eq_G.vertices[v].neighbors)
			print('---')

		S_nbs = set()
		for v in S:
			S_nbs = S_nbs | eq_G.vertices[v].neighbors

		if S_nbs != T:
			print('---')
			print('STEP 4')
			print('S = ', S, 'T = ', T)
			print(S_nbs, 'S_nbs', '/= T', T)
			y = list(S_nbs - T)[0]
			print('choose', y, 'in complement')
			z = vertex_saturated(y, M)
			if not z:
				print(y, 'unsaturated in', list(map(lambda e: e.vertices, M)))
				T.add(y)
				print('adding', y, 'to T -> T =', T)
				print('AUGMENTING MATCHING')
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
				print('NEW MATCHING', list(map(lambda e: e.vertices, M)))
				S = set()
				T = set()
				path_end = None
				print('---')
			else:
				print(y, 'saturated in', list(map(lambda e: e.vertices, M)))
				S.add(z)
				T.add(y)
				print('adding', z, 'to S -> S =', S, 'adding', y, 'to T -> T =', T)
				print('---')

	if return_type == "list":
		return list(map(lambda e: (e.vertices[0] + '-' + e.vertices[1], e.weight), M))
	elif return_type == "total":
		total = 0
		for e in M:
			total = total + e.weight
		return total

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
	'Jon': {'RB': 3, 'CAM': 2, 'GK': 1},
	'Kay': {'GK': 3, 'RW': 2, 'LW': 1, 'LB': 0}
}

print(hungarian_algorithm(ex_L, "total"))

