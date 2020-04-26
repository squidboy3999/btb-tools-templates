#! /bin/bash
# Source for creating the normal map binary - https://github.com/planrich/normalmap
# dnf install waf gcc pkg-config ImageMagick-devel
# build the binary with 'waf configure build'
# sudo cp build/normalmap /usr/bin/normalmap
mkdir ../masks_fbx
mask_files=$(find . -name "*Mask*" | cut -c 3-)
mask_files2=$(find . -name "*mask*" | cut -c 3-)
fbx_files=$(find . -name "*.fbx" | cut -c 3-)
for mask_f in ${mask_files};do
  mv ${mask_f} ../masks_fbx/
done
for mask_f2 in ${mask_files2};do
  mv ${mask_f2} ../masks_fbx/
done
for fbx_f in ${fbx_files};do
  mv ${fbx_f} ../masks_fbx/
done
for dir in $(ls -d */); do
pushd ${dir}
rename Texture Diffuse *.png
rename Texture Diffuse *.png
normal_cnt0=$(ls | grep 'normal'| wc -l)
normal_cnt1=$(ls | grep 'Normal'| wc -l)
if [ ${normal_cnt0} -lt 1 ];then
if [ ${normal_cnt1} -lt 1 ];then
dir_str=${dir%/}
normalmap $(ls| grep Diffuse) ${dir_str}_Normal.png
fi
fi
popd
done

