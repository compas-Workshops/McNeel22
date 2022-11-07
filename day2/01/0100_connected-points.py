import random
from compas.geometry import Line
from compas.geometry import Pointcloud
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


Artist.clear()

# Visualize the pointcloud points
for point in cloud:
    artist = Artist(point)
    artist.draw()

# Visualize the connection lines
for line in lines:
    artist = Artist(line)
    artist.draw()


# How would you find out how many connections any given point in the cloud has?
# How would you find a path from one point of the cloud to another, if such path exists?
# How would you find a 2-ring neighborhood of a point in the cloud?
# How ...