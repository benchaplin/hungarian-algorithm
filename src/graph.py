class Vertex: 
	def __init__(self, key):
		self.key = key
		self.label = 0
		self.indicent_edges = set()

	def set_label(self, label):
		self.label = label


class Edge:
	def __init__(self, v1, v2, weight):
		self.vertices = set([v1, v2]) # should be keys or Vertex objs?
		self.weight = weight


class Graph:
	def __init__(self):
		self.vertices = {}

	def add_vertex(self, key):
		self.vertices[key] = Vertex(key)

	def add_edge(self, v1, v2, weight):
		e = Edge(v1, v2, weight)
		self.vertices[v1].indicent_edges.add(e)


G = Graph()
G.add_vertex('a')
G.add_vertex('b')
G.add_edge('a', 'b', 1)
for e in G.vertices['a'].indicent_edges:
	print(e.vertices)