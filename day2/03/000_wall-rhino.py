import os
import compas
from compas_assembly.datastructures import Assembly
from compas.artists import Artist


HERE = os.path.dirname(__file__)
DATA = os.path.join(HERE, "wall.json")
ASSEMBLY = os.path.join(HERE, "wall-assembly.json")

# =============================================================================
# Import
# =============================================================================

assembly = compas.json_load(ASSEMBLY)

# =============================================================================
# Assembly
# =============================================================================

# =============================================================================
# Interfaces
# =============================================================================

# =============================================================================
# Boundary conditions
# =============================================================================

# =============================================================================
# Equilibrium
# =============================================================================

# =============================================================================
# Export
# =============================================================================

# =============================================================================
# Viz
# =============================================================================

Artist.clear()

artist = Artist(assembly)
artist.draw_nodes()
artist.draw_edges()
artist.draw_blocks()
artist.draw_interfaces()
artist.draw_forces(scale=5)
