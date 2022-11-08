from compas.datastructures import Mesh
from compas.colors import Color
from compas_plotters import Plotter

plotter = Plotter(figsize=(8, 8))

mesh = Mesh.from_meshgrid(dx=2, nx=2)
FACE = 1

halfedges = mesh.face_halfedges(FACE)

face_color = {
    FACE: (1.0, 0.7, 0.7),
}

meshartist = plotter.add(mesh, sizepolicy="absolute", facecolor=face_color)
meshartist.default_vertexcolor = Color.white()
meshartist.default_facecolor = Color(0.9, 0.9, 0.9)
meshartist.default_edgecolor = Color(0, 0, 0)
meshartist.draw()

meshartist.draw_vertexlabels()
meshartist.draw_facelabels()
meshartist.draw_halfedges(halfedges=halfedges, color=(1.0, 0.0, 0.0))

plotter.zoom_extents()
plotter.show()
