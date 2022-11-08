from compas.datastructures import Network
from compas.artists import Artist

# ==============================================================================
# Make Network
# ==============================================================================

network = Network()

a = network.add_node(x=0, y=0, z=0)
b = network.add_node(x=10, y=0, z=10)
c = network.add_node(x=10, y=10, z=0)
d = network.add_node(x=0, y=10, z=10)

e = network.add_node(x=5, y=5, z=0)

network.add_edge(a, e)
network.add_edge(b, e)
network.add_edge(c, e)
network.add_edge(d, e)

# ==============================================================================
# Viz
# ==============================================================================

artist = Artist(network, layer="ITA21::L6::FormFinding")

artist.clear_layer()
artist.draw()

# this is necessary to avoid that Rhino on Mac freezes up
# when you use the built-in editor to run this script
Artist.redraw()
