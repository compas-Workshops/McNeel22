import random
from compas.geometry import Line
from compas.geometry import Pointcloud
from compas.datastructures import Network
from compas.artists import Artist
from compas.colors import Color


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

# Select a random node (i.e. point in the cloud)
node = network.node_sample(size=1)[0]

# Identify the neighbours of the node
nbrs = network.neighbors(node)


Artist.clear()

# Assign a color to the random node
node_color = {node: Color.red()}

# Assign a different color to the neighbours
for nbr in nbrs:
    node_color[nbr] = Color.black()

# Assign a color to the connecting edges
edge_color = {}
for nbr in nbrs:
    edge_color[node, nbr] = Color.black()
    edge_color[nbr, node] = Color.black()

# Visualize the network
artist = Artist(network)
artist.draw_nodes(color=node_color)
artist.draw_edges(color=edge_color)
