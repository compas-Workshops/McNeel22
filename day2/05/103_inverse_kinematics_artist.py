import os

from compas_fab.backends import AnalyticalInverseKinematics
from compas_fab.backends.interfaces import ClientInterface
from compas_fab.robots import Robot
from compas_fab.robots import RobotSemantics

from compas.artists import Artist
from compas.geometry import Frame
from compas.robots import RobotModel
from compas.robots.resources import LocalPackageMeshLoader

urdf_folder = os.path.join(os.path.dirname(__file__), "../../data/robots")
urdf_file = os.path.join(urdf_folder, "ur10e.urdf")
srdf_file = os.path.join(urdf_folder, "ur10e.srdf")

model = RobotModel.from_urdf_file(urdf_file)
model.load_geometry(LocalPackageMeshLoader(urdf_folder, "ur_description"))

semantics = RobotSemantics.from_srdf_file(srdf_file, model)

client = ClientInterface()
client.inverse_kinematics = AnalyticalInverseKinematics(solver="ur10e")

robot = Robot(model, client=client, semantics=semantics)
robot.artist = Artist(model, layer="IK")

f = Frame((0.417, 0.191, -0.005), (-0.000, 1.000, 0.000), (1.000, 0.000, 0.00))

solutions = robot.iter_inverse_kinematics(f)

for config in solutions:
    robot.artist.update(config)
    robot.artist.draw()
    robot.artist.redraw(1)
    robot.artist.clear_layer()
