import os
import compas
from compas.geometry import Point, Frame, Vector, Transformation
from compas.geometry import Polyline
from compas_view2.app import App


FILE = os.path.join(os.path.dirname(__file__), "exchange.json")
GIFPATH = os.path.join(os.path.dirname(__file__), "exchange.gif")


# Load the data from the exchange file
data = compas.json_load(FILE)
curve = data["curve"]
monkey = data["monkey"]


# Define frames along the curve param space
# and corresponding transformations
frames = [curve.frame_at(t) for t in curve.space(50)]
xforms = [Transformation.from_frame_to_frame(frames[0], frame) for frame in frames]

# Define the monkey world coordinate system
monkeyworld = Frame([0, 0, 0], [0, -1, 0], [-1, 0, 0])

# Align the monkey with the frame at the start of the curve
X = Transformation.from_frame_to_frame(monkeyworld, frames[0])
monkey.transform(X)


# Create a viewer instance
viewer = App(width=1600, height=900)
viewer.view.camera.position = Point(-15, 0, 5)
viewer.view.camera.look_at(Point(0, 0, 3))

# Add te curve and the starting frame
viewer.add(curve.to_polyline())
viewer.add(frames[0])

# Add the monkey
monkeyobj = viewer.add(monkey, opacity=1.0)


# Animate the sliding
@viewer.on(interval=100, frames=len(frames), record=True, record_path=GIFPATH)
def move(f):
    viewer.add(frames[f])
    monkeyobj.matrix = xforms[f].matrix
    monkeyobj.update()


viewer.show()
