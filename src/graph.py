class Vertex: 

	def __init__(self, key):
		"""Vertex constructor.

		Parameters
		----------
		key : str, required
		"""
		self.key = key
		self.label = None
		self.neighbors = set() # keys
		self.indicent_edges = set()

	def set_label(self, label):
		"""Label the vertex."""
		self.label = label


class Edge:

	def __init__(self, v1, v2, weight = 0):
		"""Edge constructor.

		Parameters
		----------
		v1 : str, required (endpoint1 key)
		v2 : str, required (endpoint2 key)
		weight : int, optional (default = 0)
		"""
		self.vertices = frozenset([v1, v2])
		self.weight = weight

	def __eq__(self, e):
		"""Edges with equal endpoints and weights are equal."""
		return (self.vertices == e.vertices
				and self.weight == e.weight)

	def __hash__(self):
		"""Hash the vertices (frozen set) and weight."""
		return hash((self.vertices, self.weight))


class Graph:

	def __init__(self, G={}):
		"""Graph constructor.

		Parameters
		----------
		G : dict, optional (default = empty graph)
				key : vertex key
				value : set of neighboring vertices (unweighted graph)
						or 
						dict (weighted graph) 
							key : neighboring vertex key
							value : edge weight
		"""
		self.vertices = {}
		for v1 in G:
			for v2 in G[v1]:
				if type(G[v1]) is dict:
					self.add_edge(v1, v2, G[v1][v2])
				else:
					self.add_edge(v1, v2)

	def add_vertex(self, key):
		"""Add a vertex to the graph.

		Parameters
		----------
		key : str, required
		"""
		self.vertices[key] = Vertex(key)

	def add_edge(self, v1, v2, weight = 0):
		"""Add a vertex to the graph.
		
		Parameters
		----------
		v1 : str, required (endpoint1 key)
		v2 : str, required (endpoint2 key)
		weight : int, optional (default = 0)
		"""
		if v1 not in self.vertices:
			self.add_vertex(v1)
		if v2 not in self.vertices:
			self.add_vertex(v2)
		e = Edge(v1, v2, weight)
		self.vertices[v1].neighbors.add(v2)
		self.vertices[v2].neighbors.add(v1)
		self.vertices[v1].indicent_edges.add(e)
		self.vertices[v2].indicent_edges.add(e)

	def is_bipartite(self, start_vertex_key):
		return True


