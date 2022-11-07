import os
import compas
from compas_blender.conversions import BlenderMesh
from compas.artists import Artist

# To install COMPAS for Blender (Windows)
# ---------------------------------------
# This is a temp solution while we update the official installer
#
# 1. cd "%PROGRAMFILES%/Blender Foundation/Blender 3.3/3.3/python/bin"
# 2. .\python.exe -m pip install --upgrade pip
# 3. .\python.exe -m pip install compas


# Modify the path to match your system
# and the location of your workshop folder...
HOME = os.path.expanduser("~")
FILE = os.path.join(HOME, "Code", "McNeel22", "day2", "00", "exchange.json")

# Load the monkey and convert to a COMPAS mesh
mesh = BlenderMesh.from_monkey().to_compas()

# Subdivide (default scheme is catmull-clark)
mesh = mesh.subdivide(k=1)

# Export
data = {"monkey": mesh}
compas.json_dump(data, FILE)

# Visualize
Artist.clear()
artist = Artist(mesh)
artist.draw()
