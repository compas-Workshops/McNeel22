from compas.datastructures import Network
from compas.colors import Color
from compas.artists import Artist

# ==============================================================================
# Make Network
# ==============================================================================

network = Network()

network.update_default_node_attributes(is_anchor=False)

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
# Viz
# ==============================================================================

artist = Artist(network, layer="ITA21::L6::FormFinding")

nodecolor = {node: Color.red() for node in network.nodes_where(is_anchor=True)}

artist.clear_layer()
artist.draw(nodecolor=nodecolor)

# this is necessary to avoid that Rhino on Mac freezes up
# when you use the built-in editor to run this script
Artist.redraw()
