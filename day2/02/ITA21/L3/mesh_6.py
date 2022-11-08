from compas.datastructures import Mesh
from compas.colors import Color
from compas_plotters import Plotter

plotter = Plotter(figsize=(8, 8))

mesh = Mesh.from_meshgrid(dx=2, nx=2)
U = 4
V = 5

halfedges = [(U, V), (V, U)]

face_color = {
    mesh.halfedge_face(U, V): (1.0, 0.7, 0.7),
    mesh.halfedge_face(V, U): (0.7, 0.7, 1.0),
}

halfedge_color = {
    (U, V): (1.0, 0.0, 0.0),
    (V, U): (0.0, 0.0, 1.0),
}

meshartist = plotter.add(mesh, sizepolicy="absolute", facecolor=face_color)
meshartist.default_vertexcolor = Color.white()
meshartist.default_facecolor = Color(0.9, 0.9, 0.9)
meshartist.default_edgecolor = Color(0, 0, 0)
meshartist.draw()

meshartist.draw_vertexlabels()
meshartist.draw_facelabels()
meshartist.draw_halfedges(halfedges=halfedges, color=halfedge_color)

plotter.zoom_extents()
plotter.show()
