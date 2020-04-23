#! /bin/bash
for dir in $(ls -d */); do
pushd ${dir}
for tscn in $(ls *.tscn);do
sed -i "s/transform = Transform( 1, 0, 0, 0, -1.62921e-07, 1, 0, -1, -1.62921e-07, 0, 0.645235, 0 )/transform = Transform( 1, 0, 0, 0, 0.997662, -0.0683414, 0, 0.0683414, 0.997662, -4.42266e-05, 0.0352752, -6.4373e-05 )/g" ${tscn}
done
popd
done
