from jinja2 import Template

class MakeTscn:
    tres_template="/usr/local/templates/mat_template.tres.jinja"
    tscn_template="/usr/local/templates/template.tscn.jinja"
   
    def __init__(self,mv,parent_dir,logger):
        self.mv=mv
        self.parent_dir=parent_dir
        self.logger=logger
        #make tres_fp and tscn_fp from parent dir
        self.render_tres_templates()
        self.render_tscn_templates()

    def render_tres_templates(self):
        tres_file=open(self.tres_template)
        tres_string=tres_file.read()
        tres_file.close()
        template=Template(tres_string)
        jin_output = template.render(museum_name=self.mv["museum_name"],
                                 object_name=self.mv["object_name"], 
                                 diffuse_png=self.mv["diffuse_png"], 
                                 normal_png=self.mv["normal_png"])
        #write output to new_tres_fp
        tres_path=self.parent_dir+"/"+self.mv["object_name"]+".tres"
        self.logger.info("Tres file path: {}:".format(tres_path))
        self.logger.info("Jinja output: {}".format(jin_output))
        with open(tres_path,"w") as jin_f:
            jin_f.write(jin_output)

    def render_tscn_templates(self):
        tscn_file=open(self.tscn_template)
        tscn_string=tscn_file.read()
        tscn_file.close()
        template=Template(tscn_string)
        jin_output = template.render(museum_name=self.mv["museum_name"],
                                 object_name=self.mv["object_name"],
                                 object_file_name=self.mv["object_file_name"])
        #write output to new_tscn_fp
        tscn_path=self.parent_dir+"/"+self.mv["object_name"]+".tscn"
        self.logger.info("Tscn file path: {}:".format(tscn_path))
        self.logger.info("Jinja output: {}".format(jin_output))
        with open(tscn_path,"w") as jin_f:
            jin_f.write(jin_output)