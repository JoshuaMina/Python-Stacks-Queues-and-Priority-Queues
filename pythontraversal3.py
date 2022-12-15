from graph4 import connected

import networkx as nx
from graph3 import shortest_path, City, load_graph


nodes, graph = load_graph("roadmap.dot", City.from_dict)

city1 = nodes["aberdeen"]
city2 = nodes["perth"]

for i, path in enumerate(nx.all_shortest_paths(graph, city1, city2), 1):
    print(f"{i}.", " → ".join(city.name for city in path))


str = " → "


str.join(city.name for city in shortest_path(graph, city1, city2))


def by_latitude(city):
    return -city.latitude

str.join(
    city.name
    for city in shortest_path(graph, city1, city2, by_latitude)
)

print(connected(graph, nodes["belfast"], nodes["glasgow"]))

print(connected(graph, nodes["belfast"], nodes["derry"]))
