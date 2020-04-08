'''
    File name: algorithms.py
    Description: The Hungarian Method for the assignment problem.
    Author: Ben Chaplin
    GitHub: https://github.com/benchaplin/hungarian_algorithm
    Package: hungarian_algorithm
    Python Version: 3.7.5
    License: MIT License Copyright (c) 2020 Ben Chaplin
'''

from graph import Vertex, Edge, Graph


def generate_feasible_labeling(G, start_vertex_key):
	'''Generate the initial feasible labeling.

	Parameters
	----------
	G : dict, required (valid graph dict)
	start_vertex_key : str, required (any vertex)
	'''
	max = 0
	for e in G.vertices[start_vertex_key].indicent_edges:
		if e.weight > max:
			max = e.weight

	G.vertices[start_vertex_key].set_label(max)

	vertices_labeled = 1
	num_vertices = len(G.vertices)
	current_vertex = start_vertex_key

	while vertices_labeled < num_vertices:
		for v in G.vertices[current_vertex].neighbors:
			G.vertices[v].set_label(0)