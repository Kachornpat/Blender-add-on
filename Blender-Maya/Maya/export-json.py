import maya.cmds as mc
import json
from pprint import pprint
import pathlib
import re

selection = mc.ls(selection=True)

vertices = mc.ls(selection[0]+".vtx[*]", fl=1)
vertice_coor = mc.xform(vertices, q=True, ws=True, t=True)


vertice_list = []


for i in range(0,len(vertice_coor),3):
    vertice_list.append([vertice_coor[i],
                         -1*vertice_coor[i+2],
                         vertice_coor[i+1]])
    

face_connect = []
face = cmds.polyInfo( fv=True )

for f in face:
    info = re.findall("\d+",f)
    face_connect.append(list( map(int,info[1:]) ))


data = {
        "object_name": cmds.ls(sl=True)[0],
        "face_list" : face_connect,
        "vertice_index": vertice_list,
    }


path = pathlib.Path.home()/ "Desktop" / "data.json"

with open(path, "w") as output:
    text = json.dumps(data, indent=4)
    output.write(text)


print("Finish")
