from compas.geometry import Box
from compas.geometry import Frame
from compas.geometry import Translation
from compas_assembly.datastructures import Block
from compas_cra.algorithms import assembly_interfaces_numpy
from compas_cra.datastructures import CRA_Assembly
from compas_cra.equilibrium import cra_solve
from compas_assembly.viewer import DEMViewer

# =============================================================================
# Geometry
# =============================================================================

support = Box(Frame.worldXY(), 1, 1, 1)

free1 = support.transformed(Translation.from_vector([0, 0, 1]))
free1.transform(Translation.from_vector([0.1, 0.3, 0]))

# =============================================================================
# Assembly
# =============================================================================

assembly = CRA_Assembly()
assembly.add_block(Block.from_shape(support), node=0)
assembly.add_block(Block.from_shape(free1), node=1)
assembly.set_boundary_conditions([0])

# =============================================================================
# Interfaces
# =============================================================================

assembly_interfaces_numpy(assembly, nmax=10, amin=1e-2, tmax=1e-2)

# =============================================================================
# Equilibrium
# =============================================================================

cra_solve(assembly, density=1)

# =============================================================================
# Export
# =============================================================================

# =============================================================================
# Viz
# =============================================================================

viewer = DEMViewer()

viewer.add_assembly(assembly)

viewer.view.camera.zoom_extents()
viewer.run()
