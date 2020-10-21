import sys
import os
from typing import List
from PIL import Image
from pathlib import Path
from normalmap_maker import NormalMapMaker
#from fbx_convert_to_obj import  Fbx2Obj

#blender -b -P model_converter.py

class ImageConvertor:
    img_names=['.jpg','jpeg','.JPG','.JPEG','tga','dds']

    def __init__(self, file_dir):
        #dir = os.path.dirname(__file__)
        #self.parent_dir=os.path.join(dir, file_dir)
        self.parent_dir=file_dir
        print(self.parent_dir)

    def recurse_dir(self):
        results=[]
        results=self.file_actions(os.path.abspath(self.parent_dir))
        for root, subdirs, _ in os.walk(os.path.abspath(self.parent_dir)):
            for subdir in subdirs:
                full_path=os.path.join(root,subdir)
                print(full_path)
                results=results+self.file_actions(full_path)
        return results

    def file_actions(self,path):
        results=[]
        for root_sub, _, files in os.walk(path):
            for file in files:
                file_path=os.path.join(root_sub,file)
                print(file_path)
                results.append(self.action_selector(file_path))
        return results


    def action_selector(self,file_path):
        #if '.fbx' in file_path or '.FBX' in file_path:
        #    self.fbx_to_obj(file_path)
        #    return file_path+'-FBX2OBJ'
        for i_name in self.img_names:
            if i_name in file_path:
                self.img_to_png(file_path)
        self.make_normal(self.img_to_png_ext(file_path))
        return file_path+'-IMG2PNG'
    
    # def fbx_to_obj_ext(self, fbx_path):
    #     new_path=fbx_path.replace(".fbx",".obj")
    #     return new_path.replace(".FBX",".obj")

    #def fbx_to_obj(self,file_path):
    #    f2o=Fbx2Obj()
    #    f2o.obj_maker(file_path)

    def img_to_png_ext(self, img_path):
        new_path=img_path
        for i_name in self.img_names:
            new_path=new_path.replace(i_name,".png")
        return new_path

    def img_to_png(self,file_path):
        im1 = Image.open(file_path,mode='r')
        new_path=self.img_to_png_ext(file_path)
        max_size=512
        #im1=Image.open(file_path,mode='r')
        width,height=im1.size
        if width > max_size or height >max_size:
            denom=int(height/max_size)
            if width>height:
                denom=int(width/max_size)
            if denom>1:
                print('{0} is the denom'.format(denom))
                new_size=(int(width/denom),int(height/denom))
                print('new_size is {0}'.format(new_size))
                im1=im1.resize(new_size)
        im1.save(new_path,mode='r')
        os.remove(file_path)

    def make_normal(self,file_path):
        #if normal file doesn't exist
        if not os.path.isfile(file_path.replace("Diffuse.png","Normal.png")):
            nm=NormalMapMaker()
            nm.make_normal(file_path)
        # create normal maker and convert file


USAGE = f"Usage: python {sys.argv[0]} [--help] | parent_dir ]"

def run_convert(args: List[str]):
    try:
        work_dir = args[0]
    except TypeError:
        raise SystemExit(USAGE)
    img_converter=ImageConvertor(work_dir)
    img_converter.recurse_dir()

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
