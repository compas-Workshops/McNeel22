import os
import compas
from compas.colors import Color
from compas.geometry import Translation
from compas.artists import Artist

# =============================================================================
# Import
# =============================================================================

filepath = os.path.join(os.path.dirname(__file__), "wall.json")

data = compas.json_load(filepath)

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
# Viz
# =============================================================================

Artist.clear()

for course in courses:
    for box in course:
        artist = Artist(box)
        artist.draw()
