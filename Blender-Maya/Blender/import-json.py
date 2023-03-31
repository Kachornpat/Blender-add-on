import bpy
import pathlib
import json
from pprint import pprint



path = pathlib.Path.home()/ "Desktop" / "data.json"

def import_json(path):
    with open(path) as file:
        text = file.read()
        data = json.loads(text)
    return data

def create_mesh():
    data = import_json(path)
    name = data["object_name"]
    face_list = data["face_list"]
    edge = []
    vertice_index = data["vertice_index"]

    mesh = bpy.data.meshes.new(f"{name}_1")
    mesh.from_pydata(vertice_index, edge, face_list)

    mesh_object = bpy.data.objects.new(name, mesh)
    bpy.context.collection.objects.link(mesh_object)

create_mesh()
