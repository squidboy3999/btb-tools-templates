import sys
import os
from typing import List
from PIL import Image
from pathlib import Path
from normalmap_maker import NormalMapMaker
import json
from tscn_maker import MakeTscn
import logging

class ImageConverter:
    img_names=['.jpg','jpeg','.JPG','.JPEG','.tga','.dds']
    diffuse_names=['_d.png','_D.png','_diff.png','_DIFF.png','_DIFFUSE.png','_Diff.png',"_Body.png","_0.png","_NormX.png","_glow.png","_CO.png"]
    normal_names=['_n.png','_N.png','_norm.png','_NORM.png','_NORMAL.png','_Norm.png',"_NO.png","_nrm.png"]

    def __init__(self, file_dir):
        #dir = os.path.dirname(__file__)
        #self.parent_dir=os.path.join(dir, file_dir)
        self.parent_dir=file_dir
        self.rename_dict={}
        if os.path.exists("rename_dict.json"):
            with open('rename_dict.json') as jf:
                self.rename_dict=json.load(jf)
        self.create_logger()


    def create_logger(self):
        self.logger = logging.getLogger('myapp')
        hdlr = logging.FileHandler('/var/log/image_converter.log')
        formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
        hdlr.setFormatter(formatter)
        self.logger.addHandler(hdlr) 
        self.logger.setLevel(logging.INFO)

    def use_rename_dict(self,folder):
        new_name=self.rename_folder(folder)
        os.rename(folder, new_name)
        self.logger.info("Folder {} renamed to {}".format(folder,new_name))
        return new_name

    def rename_folder(self,folder):
        new_folder=folder
        for key, value in self.rename_dict.items():
            if key in folder:
                new_folder=folder.replace(key,"")
                new_folder=new_folder+value
                self.logger.info("The substring {} will be removed and the substring {} will be added".format(key,value))
        return new_folder

    def recurse_dir(self):
        results=[]
        results=self.file_actions(os.path.abspath(self.parent_dir))
        for root, subdirs, _ in os.walk(os.path.abspath(self.parent_dir)):
            for subdir in subdirs:
                full_path=os.path.join(root,subdir)
                self.logger.info("Old path name {}".format(full_path))
                new_full_path=self.use_rename_dict(full_path)
                self.logger.info("New path name {}".format(new_full_path))
                results=results+self.file_actions(new_full_path)
        return results

    def file_actions(self,path):
        results=[]
        for root_sub, _, files in os.walk(path):
            obj_name=""
            normal_name=""
            diffuse_name=""
            for file in files:
                file_path=os.path.join(root_sub,file)
                self.logger.info("File for action to be take on {}".format(file_path))
                new_path=self.action_selector(file_path)
                if ".obj" in file:
                    obj_name=file
                    self.logger.info("Object file detected - {}".format(file))
                if "_Diffuse.png" in new_path:
                    diffuse_name=new_path.split("/")[-1]
                    self.logger.info("Diffuse file located - {}".format(new_path))
                    self.logger.info("Diffuse name set to - {}".format(diffuse_name))
                if "_Normal.png" in new_path:
                    normal_name=new_path.split("/")[-1]
                    self.logger.info("Normal file located - {}".format(new_path))
                    self.logger.info("Normal name set to - {}".format(normal_name))
            #  ****** DO TSCN STUFF HERE ???
            if not obj_name =="":
                folders=root_sub.split("/")
                museum_values={"museum_name":folders[-2],
                               "object_name":folders[-1],
                               "diffuse_png":diffuse_name,
                               "normal_png":normal_name,
                               "object_file_name":obj_name}
                MakeTscn(museum_values,root_sub,self.logger)
            else:
                self.logger.warning("No object file in - {}".format(root_sub))
        # results is blank for now
        return results
    
    """
    def get_file_end(self,file_list,file_end):
        for file_path in file_list:
            if file_end in file_path:
                file_names=file_path.split("/")
                self.logger.info("File end {0} located - {1}".format(file_end,file_path))
                return file_names[-1]
        f_path=file_list[0].split("/")
        self.logger.warning("No file end {0} located in path - {1}/{2}".format(file_end,f_path[-3],f_path[-2]))
        return ""
    """

    def action_selector(self,file_path):
        #if '.fbx' in file_path or '.FBX' in file_path:
        #    self.fbx_to_obj(file_path)
        #    return file_path+'-FBX2OBJ'
        new_path=file_path
        for i_name in self.img_names:
            if i_name in file_path:
                new_path=self.img_to_png(file_path)
                if "_Diffuse.png" in new_path:
                    self.make_normal(self.img_to_png_ext(new_path))
        return new_path

    def img_to_png_ext(self, img_path):
        new_path=img_path
        for i_name in self.img_names:
            new_path=new_path.replace(i_name,".png")
            self.logger.info("Old path {0} and PNG path {1}".format(img_path,new_path))
        for d_name in self.diffuse_names:
            new_path=new_path.replace(d_name,"_Diffuse.png")
            self.logger.info("Old diffuse {0} and diffuse path {1}".format(img_path,new_path))
        for n_name in self.normal_names:
            new_path=new_path.replace(n_name,"_Normal.png")
            self.logger.info("Old normal {0} and normal path {1}".format(img_path,new_path))
        if (not "_Diffuse.png" in new_path) and (not "_Normal.png" in new_path):
            new_path=new_path.replace(".png","_Diffuse.png")
            self.logger.info("Old file {0} and new diffuse path {1}".format(img_path,new_path))
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
        self.logger.info("{} - File {} removed".format(str(not os.path.isfile(file_path)),file_path))
        self.logger.info("{} - File {} created".format(str(os.path.isfile(new_path)),new_path))
        return new_path

    def make_normal(self,file_path):
        #if normal file doesn't exist
        if not os.path.isfile(file_path.replace("Diffuse.png","Normal.png")):
            nm=NormalMapMaker()
            nm.make_normal(file_path)


USAGE = f"Usage: python {sys.argv[0]} [--help] | parent_dir ]"

def run_convert(args: List[str]):
    try:
        work_dir = args[0]
    except TypeError:
        raise SystemExit(USAGE)
    img_converter=ImageConverter(work_dir)
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
