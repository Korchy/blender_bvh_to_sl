# <pep8-80 compliant>

import bpy
from bpy.props import (StringProperty,
                       FloatProperty,
                       IntProperty,
                       BoolProperty,
                       EnumProperty,
                       )
from bpy.types import TOPBAR_MT_file_export
from bpy.utils import register_class, unregister_class
from bpy_extras.io_utils import ImportHelper, ExportHelper

if "bpy" in locals():
    import importlib
    if "export_bvh" in locals():
        importlib.reload(export_bvh)

bl_info = {
    "name": "BVH to SL",
    "author": "Campbell Barton, Andrea Rugliancich, Nikita Akimov",
    "blender": (2, 83, 13),
    "location": "File > Export",
    "description": "Unofficial fork of the original Campbell Barton's add-on for exporting BVH to SL",
    "doc_url": "{BLENDER_MANUAL_URL}/addons/import_export/anim_bvh.html",
    "category": "Import-Export"}


class BVH_TO_SL_OT_export(bpy.types.Operator, ExportHelper):
    """Save a BVH motion capture file from an armature"""
    bl_idname = "bvh_to_sl.export"
    bl_label = "Export BVH to SL"

    filename_ext = ".bvh"
    filter_glob = StringProperty(
            default="*.bvh",
            options={'HIDDEN'},
            )

    global_scale = FloatProperty(
            name="Scale",
            description="Scale the BVH by this value",
            min=0.0001, max=1000000.0,
            soft_min=0.001, soft_max=100.0,
            default=1.0,
            )
    frame_start = IntProperty(
            name="Start Frame",
            description="Starting frame to export",
            default=0,
            )
    frame_end = IntProperty(
            name="End Frame",
            description="End frame to export",
            default=0,
            )
    rotate_mode = EnumProperty(
            name="Rotation",
            description="Rotation conversion.",
            items=(('NATIVE', "Euler (Native)",
                    "Use the rotation order defined in the BVH file"),
                   ('XYZ', "Euler (XYZ)", "Convert rotations to euler XYZ"),
                   ('XZY', "Euler (XZY)", "Convert rotations to euler XZY"),
                   ('YXZ', "Euler (YXZ)", "Convert rotations to euler YXZ"),
                   ('YZX', "Euler (YZX)", "Convert rotations to euler YZX"),
                   ('ZXY', "Euler (ZXY)", "Convert rotations to euler ZXY"),
                   ('ZYX', "Euler (ZYX)", "Convert rotations to euler ZYX"),
                   ),
            default='NATIVE',
            )
    root_transform_only = BoolProperty(
            name="Root Transform Only",
            description="Only write out transform channels for the root bone",
            default=False,
            )

    @classmethod
    def poll(cls, context):
        obj = context.object
        return obj and obj.type == 'ARMATURE'

    def invoke(self, context, event):
        self.frame_start = context.scene.frame_start
        self.frame_end = context.scene.frame_end

        return super().invoke(context, event)

    def execute(self, context):
        if self.frame_start == 0 and self.frame_end == 0:
            self.frame_start = context.scene.frame_start
            self.frame_end = context.scene.frame_end

        keywords = self.as_keywords(ignore=("check_existing", "filter_glob"))

        from . import export_bvh
        return export_bvh.save(self, context, **keywords)


def menu_func_export(self, context):
    self.layout.operator(BVH_TO_SL_OT_export.bl_idname, text="Export BVH to SL (.bvh)")


def register():
    register_class(BVH_TO_SL_OT_export)

    TOPBAR_MT_file_export.append(menu_func_export)


def unregister():
    unregister_class(BVH_TO_SL_OT_export)

    TOPBAR_MT_file_export.remove(menu_func_export)


if __name__ == "__main__":
    register()