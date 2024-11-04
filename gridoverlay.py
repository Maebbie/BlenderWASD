import bpy

class HelloWorldPanel(bpy.types.Panel):
    bl_label = "Grid Scale Panel"
    bl_idname = "OBJECT_PT_hello"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'

    def draw(self, context):
        layout = self.layout
        overlay = bpy.context.space_data.overlay
        scene = context.scene

        row = layout.row()
        row.enabled = not scene.grid_lock
        row.prop(overlay, "grid_scale", text="")

        row = layout.row()
        row.alignment = 'LEFT'
        row.prop(scene, "grid_lock", text="Lock Slider", toggle=True)
        row.alignment = 'RIGHT'
        row.label(text=f"{overlay.grid_scale:.8f}")
        

def register():
    bpy.utils.register_class(HelloWorldPanel)
    bpy.types.Scene.grid_lock = bpy.props.BoolProperty(
        name="Grid Lock",
        description="Toggles lock on Grid Scale Slider, to avoid accidentally changing it via the slider above.",
        default=False
    )

def unregister():
    bpy.utils.unregister_class(HelloWorldPanel)
    del bpy.types.Scene.grid_lock

if __name__ == "__main__":
    register()
    