#! /bin/bash
museum_path=000_basic_static_objects/theme_museum
museum_path_esc=000_basic_static_objects\/theme_museum
body_path=000_static_body_parts_x-bot/000_materials
body_path_esc=000_static_body_parts_x-bot\/000_materials
for dir1 in $(ls $museum_path);do
mat_cnt=$(ls ${museum_path}/${dir1}| grep 000_materials | wc -l)
if [ $mat_cnt -gt 0 ];then
for t_file in $(ls ${museum_path}/${dir1}/000_materials/ | grep tres);do
cap_t_file_ext=$(echo "${t_file^}")
cap_t_file=$(basename ${cap_t_file_ext} .tres)
cap_dir_museum=$(echo "${dir1^}")
cap_dir=$(echo "${cap_t_file}_${cap_dir_museum}")
first_letter=$(echo $cap_t_file|head -c 1)
new_t_path=${body_path}/${first_letter}/${cap_dir}
if [ $(ls ${body_path}|grep ${first_letter} |wc -l) -lt 1 ];then
mkdir -p ${body_path}/${first_letter}
fi
file_exists=$(ls ${body_path}/${first_letter}|grep ${cap_dir} | wc -l)
if [ $file_exists -lt 1 ];then
echo ".... copying ${t_file} ...."
mkdir -p ${new_t_path}
cp ${museum_path}/${dir1}/000_materials/${t_file} ${new_t_path}
id1=$(cat ${new_t_path}/${t_file} | grep id=1 | cut -d " " -f 2| cut -d "=" -f 2 )
echo "--- id1 = ${id1} ---"
diffuse_wip=$(echo $id1 | cut -d "/" -f 8)
diffuse="${diffuse_wip%\"}"
id2=$(cat ${new_t_path}/${t_file} | grep id=2 | cut -d " " -f 2| cut -d "=" -f 2 )
echo "--- id2 = ${id2} ---"
normal_wip=$(echo $id2 | cut -d "/" -f 8)
normal="${normal_wip%\"}"
cp ${museum_path}/${dir1}/000_materials/${diffuse} ${new_t_path}
cp ${museum_path}/${dir1}/000_materials/${normal} ${new_t_path}
find_string=${museum_path_esc}\/${dir1}\/000_materials
replace_string=${body_path_esc}\/${first_letter}\/${cap_dir}
echo "... find this string: ${find_string}  ..."
echo "... replace with this string: ${replace_string}  ..."
echo "... tres file location: ${new_t_path}/${t_file}  ..."
sed -i "s/000_basic_static_objects\/theme_museum\/${dir1}\/000_materials/000_static_body_parts_x-bot\/000_materials\/${first_letter}\/${cap_dir}/g" ${new_t_path}/${t_file}
fi
done
fi
done
