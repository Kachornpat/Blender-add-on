import bpy
import bmesh
from pprint import pprint
import json
import pathlib

mesh = bpy.context.active_object


def export_json(mesh):
    bpy.ops.object.mode_set(mode="EDIT")

    bm = bmesh.from_edit_mesh(mesh.data)

    face_list = []

    for face in bm.faces:
        face_vertices = []
        for vertice in face.verts:
            face_vertices.append(vertice.index)
        face_list.append(face_vertices)
        
        
    vertice_num = len(bm.verts)
    vertice_index = [None] * vertice_num

    for vertice in bm.verts:
        vertice_index[vertice.index] = list(vertice.co)

    bpy.ops.object.mode_set(mode="OBJECT") 

    data = {
        "object_name": mesh.name,
        "face_list" : face_list,
        "vertice_index": vertice_index,
    }


    path = pathlib.Path.home()/ "Desktop" / "data.json"

    with open(path, "w") as output:
        text = json.dumps(data, indent=4)
        output.write(text)
        
export_json(mesh)
