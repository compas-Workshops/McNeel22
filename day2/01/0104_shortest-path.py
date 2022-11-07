import random
from compas.geometry import Line
from compas.geometry import Pointcloud
from compas.datastructures import Network
from compas.artists import Artist
from compas.colors import Color
from compas.utilities import pairwise


# Create a pointcloud with 83 points within given xyz bounds
cloud = Pointcloud.from_bounds(8, 5, 3, 83)

# Add connections between random pairs cloud points
lines = []
for a in cloud:
    while True:
        b = random.choice(cloud)
        if a != b:
            break
    line = Line(a, b)
    lines.append(line)


# Create a network from the connections
network = Network.from_lines(lines)

# Select two random nodes (i.e. points in the cloud)
start, end = network.node_sample(size=2)

# Find the shortest path between the nodes
path = network.shortest_path(start, end)


# Assign a color to the nodes of the path
# and a text label
node_color = {}
node_text = {}
for node in path:
    node_color[node] = Color.black()
    node_text[node] = str(node)

# Assign a different color to the start
node_color[start] = Color.red()
node_color[end] = Color.blue()

# Assign a color to the edges on the path
edge_color = {}
for u, v in pairwise(path):
    edge_color[u, v] = Color.black()
    edge_color[v, u] = Color.black()

Artist.clear()

# Visualize the network
artist = Artist(network)
artist.draw_nodes(color=node_color)
artist.draw_edges(color=edge_color)
artist.draw_nodelabels(text=node_text)
