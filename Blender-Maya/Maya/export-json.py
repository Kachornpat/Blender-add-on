import maya.cmds as mc
from pprint import pprint

selection = mc.ls(selection=True)
vertices = mc.ls(selection[0]+".vtx[*]", fl=1)

val = mc.xform(vertices, q=True, ws=True, t=True)

vertice_list = []

for i in range(0,len(val),3):
    vertice_list.append(val[i:i+3])

pprint(vertice_list[:10])
    
#pprint(val)
