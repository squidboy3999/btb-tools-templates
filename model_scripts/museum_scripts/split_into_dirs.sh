#! /bin/bash
dir_names=$(ls | cut -d '_' -f1 | cut -d '.' -f1 | sort -u)
for dir in ${dir_names};do
mkdir ${dir}
mv ${dir}_* ${dir}/
mv ${dir}.* ${dir}/
done
