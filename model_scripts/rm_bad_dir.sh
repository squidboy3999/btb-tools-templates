#! /bin/bash
for dir in $(ls -d */); do
obj_cnt=$(ls ${dir}|grep .obj|wc -l)
normal_cnt=$(ls ${dir}|grep 'ormal'|wc -l)
diffuse_cnt=$(ls ${dir}|grep 'iffuse'|wc -l)
if [ ${obj_cnt} -lt 1 ];then
rm -rf ${dir}
fi
if [ ${normal_cnt} -lt 1 ];then
rm -rf ${dir} || true
fi
if [ ${diffuse_cnt} -lt 1 ];then
rm -rf ${dir} || true
fi
done
