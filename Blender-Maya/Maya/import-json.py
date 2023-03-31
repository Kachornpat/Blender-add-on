#import maya.cmds as cmds
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

print("Finish")

#index = 0
#size = len(point)
#face_vertice = []
#for vertice in face_list[0]:
#    face_vertice.append(tuple(point[vertice]))
#    point[vertice] = index
#    index += 1
#cmds.polyCreateFacet( p=face_vertice )


#for face in face_list:
#    face_vertice = []
#    for vertice in face:
#        face_vertice.append(point[vertice])
#        if type(point[vertice]) is list:
#            point[vertice] = index
#            index += 1
#            print(f"{index}/{size} vertices")
#    cmds.polyAppendVertex( a=face_vertice )
    
#cmds.rotate( '-90deg', 0, 0, r=True )

#print("Finish")



