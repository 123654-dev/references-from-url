import bpy
from bpy_extras.io_utils import ExportHelper
from bpy.types import Operator
import os
from . urlref_save_image import save_image

class UrlRef_OT_Import(bpy.types.Operator):
    bl_idname = "urlref.import"
    bl_label = "Import!"

    def execute(self, context):
        save_image("https://global-uploads.webflow.com/623c638db44cf48bda21c5e1/62f11f92ebd5c58add3dc38d_evgeny-romanov-3-cover.jpg", bpy.context.scene.image_path)#bpy.context.scene.image_path)
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