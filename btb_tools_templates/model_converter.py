import bpy
import sys
import os
from typing import List
from PIL import Image

#blender -b -P model_converter.py

class ModelConvertor:
    jpeg_names=['.jpg','jpeg','.JPG','.JPEG']

    def __init__(self, parent_dir):
        self.parent_dir=parent_dir

    def recurse_dir(self):
        results=[]
        for root, subdirs, _ in os.walk(os.path.abspath(self.parent_dir)):
            for subdir in subdirs:
                full_path=os.path.join(root,subdir)
                for root_sub, _, files in os.walk(full_path):
                    for file in files:
                        file_path=os.path.join(root_sub,file)
                        results.append(self.action_selector(file_path))
        return results

    def action_selector(self,file_path):
        jpeg_names=['.jpg','jpeg','.JPG','.JPEG']
        if '.fbx' in file_path or '.FBX' in file_path:
            self.fbx_to_obj(file_path)
            return file_path+'-FBX2OBJ'
        for j_name in self.jpeg_names:
            if j_name in file_path:
                self.jpg_to_png(file_path)
                return file_path+'-JPG2PNG'
    
    def fbx_to_obj_ext(self, fbx_path):
        new_path=fbx_path.replace(".fbx",".obj")
        return new_path.replace(".FBX",".obj")

    def fbx_to_obj(self,file_path):
        bpy.ops.import_scene.fbx(filepath = file_path)
        bpy.ops.export_scene.obj(filepath = fbx_to_obj_ext(file_path))

    def jpg_to_png_ext(self, jpg_path):
        new_path=jpg_path
        for j_name in self.jpeg_names:
            new_path=new_path.replace(j_name,".png")
        return new_path

    def jpg_to_png(self,file_path):
        im1 = Image.open(file_path,mode='r')
        im1.save(self.jpg_to_png_ext(file_path),mode='r')

USAGE = f"Usage: python {sys.argv[0]} [--help] | parent_dir ]"

def run_convert(args: List[str]):
    try:
        parent_dir = args[0]
    except TypeError:
        raise SystemExit(USAGE)
    model_converter=ModelConvertor(parent_dir)
    model_converter.recurse_dir()

def main():
    args = sys.argv[1:]
    if not args:
        raise SystemExit(USAGE)
    if args[0] == "--help":
        print(USAGE)
    else:
        run_convert(args)

if __name__ == "__main__":
    main()