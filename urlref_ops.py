import bpy
from bpy_extras.io_utils import ExportHelper
from bpy.types import Operator
import os
from .urlref_imgutils import save_image

class UrlRef_OT_Import(bpy.types.Operator):
    bl_idname = "urlref.import"
    bl_label = "Import!"

    text: bpy.props.StringProperty(name="Enter URL", default="")

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

    def execute(self, context):
        result = save_image(self.text, bpy.context.scene.image_path)
        self.text = ""
        if result[0]:
            self.report({'INFO'}, "Image saved!")
            load_image(result[1])
        return {'FINISHED'}

class UrlRef_OT_OpenFileBrowser(Operator, ExportHelper):
    bl_idname = "urlref.open_filebrowser"
    bl_label = "Change Image Folder"
    filename_ext = "."
    use_filter_folder = True

    def invoke(self, context, event):
        if bpy.data.is_saved:
            self.filepath = ""
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'} 

    def execute(self, context):
        userpath = self.properties.filepath
        if( not os.path.isdir(userpath)):
            msg = "Please select a directory not a file: " + userpath
            self.report({'WARNING'}, msg)
        else:
            print(self.filepath)
            bpy.context.scene.image_path = self.filepath  
        return {'FINISHED'}

def load_image(path):
    bpy.ops.object.load_reference_image(filepath=path)