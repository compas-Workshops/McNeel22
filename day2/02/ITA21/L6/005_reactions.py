from compas.geometry import Point
from compas.geometry import Vector
from compas.datastructures import Network
from compas.colors import Color
from compas.artists import Artist

# ==============================================================================
# Make Network
# ==============================================================================

network = Network()

network.update_default_node_attributes(is_anchor=False)
network.update_default_node_attributes(residual=None)
network.update_default_edge_attributes(force=1.0)

a = network.add_node(x=0, y=0, z=0, is_anchor=True)
b = network.add_node(x=10, y=0, z=10, is_anchor=True)
c = network.add_node(x=10, y=10, z=0, is_anchor=True)
d = network.add_node(x=0, y=10, z=10, is_anchor=True)

e = network.add_node(x=5, y=5, z=0)

network.add_edge(a, e)
network.add_edge(b, e)
network.add_edge(c, e)
network.add_edge(d, e)

# ==============================================================================
# Compute Residuals
# ==============================================================================

for node in network.nodes():
    a = Point(*network.node_coordinates(node))

    residual = Vector(0, 0, 0)

    for nbr in network.neighbors(node):
        b = Point(*network.node_coordinates(nbr))

        edge = (node, nbr) if network.has_edge(node, nbr) else (nbr, node)
        force = network.edge_attribute(edge, "force")

        ab = b - a
        ab.unitize()
        ab.scale(force)

        residual += ab

    network.node_attribute(node, "residual", residual)

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

    if network.node_attribute(node, "is_anchor"):
        artist = Artist(residual.scaled(-1), color=Color.green(), layer="ITA21::L6::FormFinding")
    else:
        artist = Artist(residual, color=Color.cyan(), layer="ITA21::L6::FormFinding")

    artist.draw(point=point)

# this is necessary to avoid that Rhino on Mac freezes up
# when you use the built-in editor to run this script
Artist.redraw()
