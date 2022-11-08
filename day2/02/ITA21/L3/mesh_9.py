from compas.datastructures import Mesh
from compas.colors import Color
from compas_plotters import Plotter

plotter = Plotter(figsize=(8, 8))

mesh = Mesh.from_meshgrid(dx=2, nx=2)
U, V = 4, 5
V, W = mesh.halfedge_after(U, V)

halfedges = [(U, V), (V, W), (W, V)]

face_color = {
    mesh.halfedge_face(V, W): (1.0, 0.7, 0.7),
}

halfedge_color = {
    (U, V): (1.0, 0.0, 0.0),
    (V, W): (1.0, 0.0, 0.0),
    (W, V): (0.0, 0.0, 1.0),
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
