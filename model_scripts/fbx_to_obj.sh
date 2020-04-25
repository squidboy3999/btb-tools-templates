#! /bin/bash
# dnf install assimp -y
for dir in $(ls -d */); do
pushd ${dir}
for f in $(ls | grep .fbx);do
file_name=${f%.fbx}
assimp export <file_name>.fbx <file_name>.obj
done
popd
done
