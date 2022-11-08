import os
import compas
from compas.geometry import Translation
from compas.geometry import Line
from compas.datastructures import Mesh
from compas_assembly.datastructures import Assembly
from compas_assembly.algorithms import assembly_interfaces
from compas_assembly.viewer import DEMViewer
from compas_cra.equilibrium import cra_solve


HERE = os.path.dirname(__file__)
DATA = os.path.join(HERE, "wall.json")
ASSEMBLY = os.path.join(HERE, "wall-assembly.json")

# =============================================================================
# Import
# =============================================================================

data = compas.json_load(DATA)

params = data["params"]
curve = data["basecurve"]
course_0 = data["courses"][0]
course_1 = data["courses"][1]

# =============================================================================
# Courses
# =============================================================================

courses = []

for i in range(10):
    boxes = course_1 if i % 2 else course_0
    courses.append([box.transformed(Translation.from_vector([0, 0, i * box.zsize])) for box in boxes])

# =============================================================================
# Assembly
# =============================================================================

assembly = Assembly()

for course in courses:
    for box in course:
        assembly.add_block_from_mesh(Mesh.from_shape(box))

# =============================================================================
# Interfaces
# =============================================================================

assembly_interfaces(assembly, tmax=1e-6, amin=1e-2)

# =============================================================================
# Boundary conditions
# =============================================================================

assembly.unset_boundary_conditions()

nodes = sorted(assembly.nodes(), key=lambda node: assembly.node_point(node)[2])[: params["N"] - 1]
for node in nodes:
    assembly.set_boundary_condition(node)

# =============================================================================
# Equilibrium
# =============================================================================

cra_solve(assembly)

# =============================================================================
# Export
# =============================================================================

compas.json_dump(assembly, ASSEMBLY)

# =============================================================================
# Viz
# =============================================================================

viewer = DEMViewer()
viewer.view.camera.position = [-1, -8, 3]
viewer.view.camera.look_at([3, 0, 2])

viewer.add_assembly(assembly)

viewer.run()
