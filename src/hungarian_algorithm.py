from graph import Vertex, Edge, Graph


def generate_feasible_labeling(G, start_vertex_key):
	"""Add a vertex to the graph.

	Parameters
	----------
	G : dict, required (valid graph dict)
	start_vertex_key : str, required (any vertex)
	"""
	max = 0
	for e in G.vertices[start_vertex_key].indicent_edges:
		if e.weight > max:
			max = e.weight
	print('setting %s label:' % start_vertex_key, max)
	G.vertices[start_vertex_key].set_label(max)

	vertices_labeled = 1
	num_vertices = len(G.vertices)
	current_vertex = start_vertex_key
	while vertices_labeled < num_vertices:
		for v in G.vertices[current_vertex].neighbors:
			print('setting %s label: 0' % v)
			G.vertices[v].set_label(0)