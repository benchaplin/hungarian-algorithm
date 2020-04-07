# Hungarian Algorithm

A Python 3 implementation of the Hungarian Algorithm (a.k.a. the Kuhn-Munkres algorithm), an O(n^3) solution for the assignment problem, or maximum-weighted bipartite matching problem.

## Usage

### Import 

```python
from hungarian-algorithm import hungarian_algorithm
```
### Inputs

Define your weighted bipartite graph in the following manner:

```python
G = {
	'a': {'b': 2, 'c': 7, 'e': 1},
	'b': {'a': 2, 'd': 5, 'e': 0},
	'c': {'a': 7},
	'd': {'b': 5},
	'e': {'a': 1 , 'b': 0}
}
```

thus defining a graph G = (V, E) with vertex set V = {a, b, c, d, e} and edge set E = {(a, b), (a, c), (a, e), (b, d), (b, e)}.

Then pass the graph as an input:

```python
hungarian_algorithm(G)
```

## History

The algorithm was published by Harold Kuhn in 1955 paper "The Hungarian Method for the Assignment Problem." Kuhn's work relied heavily on that of Hungarian mathematicians D&eacute;nes K&#337;nig and Jen&#337; Eg&eacute;vary. 
