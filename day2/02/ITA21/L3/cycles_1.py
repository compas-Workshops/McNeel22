from compas.datastructures import Mesh
from compas.colors import Color
from compas_plotters import Plotter

plotter = Plotter(figsize=(8, 8))

mesh = Mesh.from_meshgrid(dx=2, nx=2)

VERTEX = 4

nbrs = mesh.vertex_neighbors(VERTEX)

vertex_color = {VERTEX: (1.0, 0.0, 0.0), nbrs[0]: (0.0, 0.0, 1.0)}

meshartist = plotter.add(mesh, sizepolicy="absolute", vertexcolor=vertex_color)
meshartist.default_vertexcolor = Color.white()
meshartist.default_facecolor = Color(0.9, 0.9, 0.9)
meshartist.default_edgecolor = Color(0, 0, 0)
meshartist.draw()

plotter.zoom_extents()
plotter.show()
