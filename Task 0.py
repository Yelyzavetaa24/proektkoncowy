# installResources.py

import subprocess

components = [
    "component1",
    "component2",
    "component3"
]

for component in components:
    subprocess.call(["pip", "install", component])
