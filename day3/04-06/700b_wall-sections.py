from itertools import groupby
import os
from collections import deque
import compas
from compas.artists import Artist
from compas.colors import ColorMap, Color

HERE = os.path.dirname(__file__)
ASSEMBLY = os.path.join(HERE, "wall-assembly.json")

# =============================================================================
# Import
# =============================================================================

assembly = compas.json_load(ASSEMBLY)

# =============================================================================
# Courses
# =============================================================================

assembly.graph.update_default_node_attributes(course=None)

groups = []

for key, group in groupby(assembly.nodes(), lambda n: "{:.1f}".format(assembly.node_point(n).z)):
    for node in group:
        assembly.graph.node_attribute(node, "course", key)
    groups.append(key)

# =============================================================================
# Traverse
# =============================================================================

node = 31
tovisit = deque([node])
visited = set([node])
ordering = [node]
while tovisit:
    node = tovisit.popleft()
    for nbr in assembly.graph.neighbors(node):
        if nbr not in visited:
            if assembly.node_point(nbr).z < assembly.node_point(node).z:
                visited.add(nbr)
                tovisit.append(nbr)
                ordering.append(nbr)

print(ordering)

# =============================================================================
# Equilibrium
# =============================================================================

# =============================================================================
# Export
# =============================================================================

# compas.json_dump(assembly, ASSEMBLY)

# =============================================================================
# Viz
# =============================================================================

cmap = ColorMap.from_color(Color.red())

node_color = {}
for index, key in enumerate(groups):
    color = cmap(index, 0, len(groups) - 1)
    for node in assembly.graph.nodes_where(course=key):
        node_color[node] = color

Artist.clear()

artist = Artist(assembly)
artist.draw_nodes(color=node_color)
artist.draw_edges()
artist.draw_blocks(color=node_color)
