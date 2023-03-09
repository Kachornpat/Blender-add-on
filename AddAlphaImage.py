bl_info = {
    "name": "Add Alpha Image Texture",
    "author": "Kachornpat G.",
    "version": (1, 0),
    "blender": (3, 4, 1),
    "location": "Shader > Tool",
    "warning": "",
    "wiki_url": "",
    "category": "Add Image"
}


import bpy


class AlphaImagePanel(bpy.types.Panel):
    
    bl_label = "Alpha Image"
    bl_idname = "AlphaImage"
    bl_space_type = 'NODE_EDITOR'
    bl_region_type = 'UI'
    bl_category = "Alpha"

    def draw(self, context):
        layout = self.layout

        obj = context.object

        row = layout.row()
        row.operator('shader.add_alpha_operator', text="Add Alpha Image", icon="IMAGE")


class ALPHA_IMAGE(bpy.types.Operator):
    bl_label = "Create Alpha Image"
    bl_idname = "shader.add_alpha_operator"
    
    name: bpy.props.StringProperty(name="Name", default="")
    width: bpy.props.IntProperty(name="Width", default=4096)
    height: bpy.props.IntProperty(name="Height", default=2560)
    
    
    def execute(self, context):
        
        cur_material = bpy.data.materials[1]
        cur_material.use_nodes = True
        
        active_node = cur_material.node_tree.nodes.active
        
        texImage = bpy.data.materials[1].node_tree.nodes.new(type="ShaderNodeTexImage")
        texImage.location = (active_node.location.x-300, active_node.location.y)
        
        cur_material.node_tree.links.new(texImage.outputs[0], active_node.inputs[0])
        
        alpha_image = bpy.data.images.new(name=self.name, alpha=True, width=self.width, height=self.height)
        texImage.image = alpha_image
        
        cur_material.node_tree.nodes.active = texImage
    
        return {"FINISHED"}
    
    def invoke(self, context, event):
        
        return context.window_manager.invoke_props_dialog(self)
        

def register():
    bpy.utils.register_class(ALPHA_IMAGE)
    bpy.utils.register_class(AlphaImagePanel)
    


def unregister():
    bpy.utils.unregister_class(ALPHA_IMAGE)
    bpy.utils.unregister_class(AlphaImagePanel)
    

if __name__ == "__main__":
    register()
