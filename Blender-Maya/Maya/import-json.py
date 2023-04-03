import maya.cmds as cmds
import maya.api.OpenMaya as om
import json
import pathlib
path = pathlib.Path.home()/ "Desktop" / "data.json"

with open(path) as file:
    text = file.read()
    data = json.loads(text)
    
point = data["vertice_index"]   
face_list = data["face_list"]

vertices = [om.MPoint(p[0], p[2], -1*p[1]) for p in point]
polygonFaces = [len(f) for f in face_list]


meshFn = om.MFnMesh()

polygonConnects = []

for f in face_list:
    for index in f:
        polygonConnects.append(index)

meshFn.create(vertices, polygonFaces, polygonConnects )
name = cmds.ls("*polySurface*")
cmds.rename(name[-1], data["object_name"]) 
print("Finish")



