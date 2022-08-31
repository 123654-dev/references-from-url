import bpy
from bpy.types import Panel

class UrlRef_PT_MainPanel(bpy.types.Panel):
    bl_label = "Reference from URL"
    bl_idname = "PT_TestPanel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "New Tab"
    
    def draw(self, context):
        layout = self.layout
        
        row = layout.row()
        row.label(text="Settings", icon="PREFERENCES")
        row = layout.row()
        row.label(text="Defaults to ./urlref")
        row = layout.row()
        row.operator("urlref.open_filebrowser", icon="RIGHTARROW_THIN")
        
        sep = layout.separator()
        
        row = layout.row()
        row.label(text="Image Import", icon="OUTPUT")
        row = layout.row()
        row.prop(context.scene, "current_url_name", icon="LINKED")
        row = layout.row()
        col = row.column()
        col.operator("urlref.import", icon="RIGHTARROW_THIN")