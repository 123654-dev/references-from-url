bl_info = {"name": "Reference from URL", "author":"123654-dev", "version":(0,0,1), "blender":(2, 80, 0), "location": "View3D > Toolbar", "description": "Reference from URL", "category": "Import"}

import bpy

from . urlref_ops import UrlRef_OT_Import, UrlRef_OT_OpenFileBrowser
from . urlref_panel import UrlRef_PT_MainPanel

classes = (UrlRef_OT_Import, UrlRef_PT_MainPanel, UrlRef_OT_OpenFileBrowser)
	
def register():
    bpy.types.Scene.image_path = bpy.props.StringProperty(name="urlref.image_path", default="/urlref")
    bpy.types.Scene.image_url = bpy.props.StringProperty(name="urlref.image_path")

    for cls in classes:
	    bpy.utils.register_class(cls)

def unregister():
    del bpy.types.Scene.image_path
    for cls in classes:
        bpy.utils.unregister_class(cls)