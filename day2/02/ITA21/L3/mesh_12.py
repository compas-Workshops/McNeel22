from compas.datastructures import Mesh
from compas.colors import Color
from compas_plotters import Plotter

plotter = Plotter(figsize=(8, 8))

mesh = Mesh.from_meshgrid(dx=10, nx=10)

vertex_color = {vertex: (1.0, 0.0, 0.0) for vertex in mesh.vertices()}
vertex_color.update({vertex: (0.0, 0.0, 1.0) for vertex in mesh.vertices_on_boundary()})

meshartist = plotter.add(mesh, sizepolicy="relative", vertexsize=10, vertexcolor=vertex_color)
meshartist.default_vertexcolor = Color.white()
meshartist.default_facecolor = Color(0.9, 0.9, 0.9)
meshartist.default_edgecolor = Color(0, 0, 0)
meshartist.draw()

plotter.zoom_extents()
plotter.show()
