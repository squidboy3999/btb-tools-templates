#! /bin/bash
path=$(pwd)
museum_name=$(basename ${path})
for dir in $(ls -d */); do
pushd ${dir}
dir_str=${dir%/}
cp ../../templates/* .
mv mat_template.tres ${dir_str}.tres
diffuse=$(ls *.png| grep Diffuse|awk '{print $1; exit}')
normal=$(ls *.png| grep Normal|awk '{print $1; exit}')
sed -i "s/<diffuse_png>/$diffuse/g" ${dir_str}.tres
sed -i "s/<normal_png>/$normal/g" ${dir_str}.tres
sed -i "s/<museum_name>/$museum_name/g" ${dir_str}.tres
sed -i "s/<object_name>/$dir_str/g" ${dir_str}.tres
for obj in $(ls *.obj);do
obj_name=${obj%.*}
cp template.tscn ${obj_name}.tscn
sed -i "s/<museum_name>/$museum_name/g" ${obj_name}.tscn
sed -i "s/<object_name>/$dir_str/g" ${obj_name}.tscn
sed -i "s/<obj_file_name>/$obj/g" ${obj_name}.tscn
done
popd
done
