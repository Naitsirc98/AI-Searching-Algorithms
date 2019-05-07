# Search methods

import search

ab = search.GPSProblem('A', 'B'
                       , search.romania)

print("\n=== Breath search === ")
print(search.breadth_first_graph_search(ab))

print("\n=== Depth search === ")
print(search.depth_first_graph_search(ab))

print("\n=== Branch and Bound search === ")
print(search.acotation_graph_search(ab))

print("\n=== Branch and Bound (heuristic) search === ")
print(search.heuristic_graph_search(ab))

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
