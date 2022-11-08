import time
import compas_rhino
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
# Helper Function for Computing the Residual at a Node
# ==============================================================================


def compute_residual(network, node):
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

    return residual


# ==============================================================================
# Viz Helper
# ==============================================================================


def draw():
    artist.draw_nodes(color=nodecolor)
    artist.draw_edges()

    for node in network.nodes():
        point = Point(*network.node_coordinates(node))
        residual = network.node_attribute(node, "residual")

        if network.node_attribute(node, "is_anchor"):
            vector = residual.scaled(-1)
            color = Color.green()
        else:
            vector = residual
            color = Color.cyan()

        Artist(vector, color=color, layer="ITA21::L6::FormFinding").draw(point=point)

    Artist.redraw()
    compas_rhino.wait()


# ==============================================================================
# Initial State
# ==============================================================================

for node in network.nodes():
    residual = compute_residual(network, node)
    network.node_attribute(node, "residual", residual)

nodecolor = {node: Color.red() for node in network.nodes_where(is_anchor=True)}

artist = Artist(network, layer="ITA21::L6::FormFinding")
artist.clear_layer()
artist.redraw()

draw()
time.sleep(1.0)

# ==============================================================================
# Update Geometry and Viz
# ==============================================================================

for _ in range(100):
    # 1. compute all residuals in the current geometry
    # 2. move the free nodes in the direction of the residual

    for node in network.nodes():
        residual = compute_residual(network, node)
        network.node_attribute(node, "residual", residual)

        if network.node_attribute(node, "is_anchor"):
            continue

        residual = network.node_attribute(node, "residual")
        point = Point(*network.node_attributes(node, ["x", "y", "z"]))
        newpoint = point + residual

        network.node_attributes(node, ["x", "y", "z"], newpoint)

    # 3. compute all residuals in the new geometry

    for node in network.nodes():
        residual = compute_residual(network, node)
        network.node_attribute(node, "residual", residual)

    # 4. visualize

    draw()
