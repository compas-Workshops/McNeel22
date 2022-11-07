import random
from compas.geometry import Line
from compas.geometry import Pointcloud
from compas.datastructures import Network
from compas.artists import Artist


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


Artist.clear()

# Visualize the network
artist = Artist(network)
artist.draw()
