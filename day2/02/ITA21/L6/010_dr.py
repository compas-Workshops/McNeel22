from compas.geometry import Point
from compas.geometry import Vector
from compas.datastructures import Network
from compas.artists import Artist
from compas.colors import Color
from compas.numerical import dr

# ==============================================================================
# Make Network
# ==============================================================================

network = Network()

network.update_default_node_attributes(is_anchor=False)
network.update_default_node_attributes(residual=None)
network.update_default_node_attributes(px=0, py=0, pz=0)

network.update_default_edge_attributes(qpre=1.0)
network.update_default_edge_attributes(fpre=0.0)

a = network.add_node(x=0, y=0, z=0, is_anchor=True)
b = network.add_node(x=10, y=0, z=10, is_anchor=True)
c = network.add_node(x=10, y=10, z=0, is_anchor=True)
d = network.add_node(x=0, y=10, z=10, is_anchor=True)

e = network.add_node(x=5, y=5, z=0)

network.add_edge(a, e)
network.add_edge(b, e, qpre=1.0)
network.add_edge(c, e)
network.add_edge(d, e)

# ==============================================================================
# Dynamic Relaxation
# ==============================================================================

xyz = network.nodes_attributes(["x", "y", "z"])
edges = list(network.edges())
fixed = list(network.nodes_where(is_anchor=True))
loads = network.nodes_attributes(["px", "py", "pz"])
qpre = network.edges_attribute("qpre")
fpre = network.edges_attribute("fpre")

result = dr(xyz, edges, fixed, loads, qpre=qpre, fpre=fpre, kmax=100)

for node in network.nodes():
    network.node_attributes(node, ["x", "y", "z"], result[0][node])
    network.node_attribute(node, "residual", Vector(*result[-1][node]))

# ==============================================================================
# Viz
# ==============================================================================

artist = Artist(network, layer="ITA21::L6::FormFinding")

nodecolor = {node: Color.red() for node in network.nodes_where(is_anchor=True)}

artist.clear_layer()
artist.draw(nodecolor=nodecolor)

for node in network.nodes():
    point = Point(*network.node_coordinates(node))
    residual = network.node_attribute(node, "residual")

    if residual.length < 0.01:
        continue

    if network.node_attribute(node, "is_anchor"):
        artist = Artist(residual.scaled(-1), color=Color.green(), layer="ITA21::L6::FormFinding")
    else:
        artist = Artist(residual, color=Color.cyan(), layer="ITA21::L6::FormFinding")

    artist.draw(point=point)

# this is necessary to avoid that Rhino on Mac freezes up
# when you use the built-in editor to run this script
Artist.redraw()
