#! /bin/bash
parent_dir=${PWD##*/}
script_name=$(echo "$parent_dir" | tr '[:upper:]' '[:lower:]')
tscn_list=$(find . -name "*.tscn")
