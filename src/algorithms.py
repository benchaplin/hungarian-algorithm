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


def generate_feasible_labeling(G, start_vertex):
	'''Generate the initial feasible labeling.

	Parameters
	----------
	G : Graph, required
	start_vertex : str, required (any vertex key)

	Return
	----------
	bool : True if bipartite and labeling generated,
		   False if not bipartite and labeling
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

def hungarian_algorithm(_G):
	'''Find maximum-weighted matching.

	Parameters
	----------
	_G : dict, required (valid Graph dict)

	Return
	----------

	'''
	G = Graph(_G)
	start_vertex = list(G.vertices.keys())[0]

	G.generate_feasible_labeling(start_vertex)
	eq_G = G.equality_subgraph()

	for v in eq_G.vertices:
		print(v, "nbs:", eq_G.vertices[v].neighbors, "ind edges", list(map(lambda e: (e.vertices, e.weight), eq_G.vertices[v].indicent_edges)))




ex_H = {
	'x1': {'y1': 1, 'y2': 6},
	'x2': {'y2': 8, 'y3': 6},
	'x3': {'y1': 4, 'y3': 1}
}

hungarian_algorithm(ex_H)









