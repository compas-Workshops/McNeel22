import os
import compas
from compas.geometry import Box
from compas.geometry import Frame
from compas.geometry import Translation
from compas_assembly.datastructures import Assembly
from compas_assembly.datastructures import Block
from compas_assembly.algorithms import assembly_interfaces
from compas_assembly.viewer import DEMViewer
from compas_cra.equilibrium import cra_solve

HERE = os.path.dirname(__file__)
ASSEMBLY = os.path.join(HERE, "two-blocks-assembly.json")

# =============================================================================
# Geometry
# =============================================================================

base = Box(Frame.worldXY(), 1, 1, 1)

box1 = base.copy()
box2 = base.transformed(Translation.from_vector([0, 0, base.zsize]))

# =============================================================================
# Assembly
# =============================================================================

assembly = Assembly()
assembly.add_block(Block.from_shape(box1), node=0)
assembly.add_block(Block.from_shape(box2), node=1)

# =============================================================================
# Interfaces
# =============================================================================

assembly_interfaces(assembly, nmax=10, amin=1e-2, tmax=1e-2)

# =============================================================================
# Boundary conditions
# =============================================================================

assembly.set_boundary_condition(0)

# =============================================================================
# Equilibrium
# =============================================================================

cra_solve(assembly)

# =============================================================================
# Export
# =============================================================================

# compas.json_dump(assembly, ASSEMBLY)

# =============================================================================
# Viz
# =============================================================================

viewer = DEMViewer()
viewer.view.camera.position = [0, -7, 1]
viewer.view.camera.look_at([0, 0, 0])

viewer.add_assembly(assembly)

viewer.run()
