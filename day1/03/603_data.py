import os
import compas

filepath = os.path.join(os.path.dirname(__file__), "session.json")

data = compas.json_load(filepath)

curve = data['curve']
box = data['box']

print(curve)
print(box)
