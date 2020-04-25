#! /bin/bash
# dnf install assimp -y
file_name=${f%.fbx}
assimp export <file_name>.fbx <file_name>.obj
