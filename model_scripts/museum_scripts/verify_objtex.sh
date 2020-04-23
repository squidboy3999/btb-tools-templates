#! /bin/bash
touch missing_tex.txt
touch missing_normal.txt
touch missing_obj.txt
for dir in $(ls);do
pushd ${dir}
obj_cnt=$(ls | grep .obj | wc -l)
if [ 1 -gt ${obj_cnt} ]; then
echo ${dir} >> ../missing_obj.txt
fi
normal_cnt=$(ls | grep ormal | wc -l)
if [ 1 -gt ${normal_cnt} ]; then
echo ${dir} >> ../missing_normal.txt
fi
png_cnt=$(ls | grep .png | wc -l)
jpg_cnt=$(ls | grep .jpg | wc -l)
jpeg_cnt=$(ls | grep .jpeg | wc -l)
if [ 1 -gt ${png_cnt} ] && [ 1 -gt ${jpg_cnt} ] && [ 1 -gt ${jpeg_cnt} ]; then
echo ${dir} >> ../missing_tex.txt
fi
popd
done
