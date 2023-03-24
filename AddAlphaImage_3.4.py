bl_info = {
    "name": "Alpha Image",
    "author": "Kachornpat G.",
    "version": (1, 1),
    "blender": (3, 4, 1),
    "location": "Shader > Tool",
    "description": "Add Alpha Image Texture",
    "warning": "",
    "doc_url": "https://github.com/Kachornpat/Blender-add-on.git",
    "category": "Material",
}


import bpy


class AlphaImagePanel(bpy.types.Panel):
    
    bl_label = "Alpha Image"
    bl_idname = "AlphaImage"
    bl_space_type = 'NODE_EDITOR'
    bl_region_type = 'UI'
    bl_category = "Tool"

    def draw(self, context):
        layout = self.layout

        obj = context.object

        row = layout.row()
        row.operator('shader.add_alpha_operator', text="Add Alpha Image", icon="IMAGE")


class ALPHA_IMAGE(bpy.types.Operator):
    bl_label = "Create Alpha Image"
    bl_idname = "shader.add_alpha_operator"
    
    def update_resolution(self, context):
        if self.resolution == "OP1":
            self.width = 4096
            self.height = 4096
        elif self.resolution == "OP2":
            self.width = 2048
            self.height = 2048
        elif self.resolution == "OP3":
            self.width = 1920
            self.height = 1920
    
    def update_resolution_2(self, context):
        if self.resolution_2 == "OP1":
            self.width_2 = 4096
            self.height_2 = 4096
        elif self.resolution == "OP2":
            self.width_2 = 2048
            self.height_2 = 2048
        elif self.resolution_2 == "OP3":
            self.width_2 = 1920
            self.height_2 = 1920
            
    resolution_list = [('OP1', "4K", "resolution 4096x4096"),
                       ('OP2', "2K", "resolution 2048x2048"),
                       ('OP3', "1K", "resolution 1920x1920"),
                      ]
    
    name: bpy.props.StringProperty(name="First image: Name", default="")
    resolution: bpy.props.EnumProperty(name="Resolution", 
                                       description="Select an option",
                                       items=resolution_list,
                                       update=update_resolution)
    width: bpy.props.IntProperty(name="Width", default=4096)
    height: bpy.props.IntProperty(name="Height", default=4096)
    alpha: bpy.props.BoolProperty(name="Alpha", default=True)
    
    
    name_2: bpy.props.StringProperty(name="Second image: Name", default="")
    resolution_2: bpy.props.EnumProperty(name="Resolution", 
                                       description="Select an option",
                                       items=resolution_list,
                                       update=update_resolution_2)
    width_2: bpy.props.IntProperty(name="Width", default=4096)
    height_2: bpy.props.IntProperty(name="Height", default=4096)
    alpha_2: bpy.props.BoolProperty(name="Alpha", default=True)
    
    
    def execute(self, context):
        
        if self.name == "" or self.name_2 == "":
            self.report({"ERROR"}, "Please enter all the name inputs.")
        
        elif bpy.data.images.get(self.name) != None or bpy.data.images.get(self.name_2) != None:
            self.report({"ERROR"}, "At least one of the names already exists, please try a new name.")
        
        else:
        
            cur_material = bpy.context.active_object.active_material
            cur_material.use_nodes = True
            
            active_node = cur_material.node_tree.nodes.active
            

            if active_node is None:
                active_node = cur_material.node_tree.nodes[-1]
            
            texImage = cur_material.node_tree.nodes.new(type="ShaderNodeTexImage")
            texImage.location = (active_node.location.x-600, active_node.location.y)
            
            mix = cur_material.node_tree.nodes.new(type="ShaderNodeMix")
            mix.data_type = "RGBA"
            mix.location = (active_node.location.x-250, active_node.location.y)
            
                 
            cur_material.node_tree.links.new(mix.outputs[2], active_node.inputs[0])
            cur_material.node_tree.links.new(texImage.outputs[0], mix.inputs[6])
            
            
            bpy.ops.image.new(name=self.name, 
                              alpha=self.alpha, 
                              width=self.width, 
                              height=self.height, 
                              color=(0,0,0,0))
            alpha_image_1 = bpy.data.images.get(self.name)
            texImage.image = alpha_image_1

            texImage_2 = cur_material.node_tree.nodes.new(type="ShaderNodeTexImage")
            texImage_2.location = (active_node.location.x-600, active_node.location.y-300)
            
            bpy.ops.image.new(name=self.name_2, 
                              alpha=self.alpha_2, 
                              width=self.width_2, 
                              height=self.height_2, 
                              color=(0,0,0,0))
            alpha_image_2 = bpy.data.images.get(self.name_2)
            texImage_2.image = alpha_image_2
            
            cur_material.node_tree.links.new(texImage_2.outputs[0], mix.inputs[7])
            
            self.name = ""
        

#        cur_material.node_tree.nodes.active = texImage

    
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
