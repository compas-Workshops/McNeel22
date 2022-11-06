from compas.geometry import Point
from compas.geometry import NurbsCurve
from compas.geometry import Box
from compas.geometry import Frame
from compas.geometry import Transformation
from compas.utilities import linspace
from compas.artists import Artist

points = [
    Point(0, 0, 0),
    Point(3, 3, 0),
    Point(6, -6, 3),
    Point(9, 0, 0),
]
curve = NurbsCurve.from_points(points)

frames = []
for t in linspace(curve.domain[0], curve.domain[1], 10):
    frames.append(curve.frame_at(t))

box = Box(Frame.worldXY(), 0.8, 0.5, 0.3)

boxes = []
for frame in frames:
    transformation = Transformation.from_frame_to_frame(box.frame, frame)
    boxes.append(box.transformed(transformation))

Artist.clear()

artist = Artist(curve)
artist.draw()

for frame in frames:
    artist = Artist(frame, scale=0.5)
    artist.draw()

for box in boxes:
    artist = Artist(box)
    artist.draw()
