#! /bin/bash
parent_dir=${PWD##*/}
script_name=$(echo "$parent_dir" | tr '[:upper:]' '[:lower:]')
script_path="../../../../code/data_components/game_boards/template_museums/${script_name}.gd"
touch ${script_path}
echo "# objects are assumed to be 1x1 squares or 1/9th of a tile space
# objects lists of 2 itesms: model name and hp of object
# future work may include other sizes

#helper strings for the arrays
var char_path=\"theme_museum/${parent_dir}/\"
var outside_object_path=\"\"
var hp=1000

var inside_objects=gen_inside_obj()
var outside_objects=inside_objects

func gen_inside_obj():
	var tmp=[]">>${script_path}
tscn_list=$(find . -name "*.tscn")
for tscn in ${tscn_list};do 
new_name=$(echo ${tscn} | cut -c3-)
tscn_path=${new_name%.tscn}
echo "	tmp.append([char_path+\"${tscn_path}\",hp])">>${script_path}
done
echo "	return tmp


# saturation is the number of objects to place in a single tile, 1,2, or 3
var saturation=3
# level object count is the number of rows and columns that will have objects 
# on them - 1 to 60, should be based on object count, and how many repeats 
# there should be.
var level_object_count=30">>${script_path}
