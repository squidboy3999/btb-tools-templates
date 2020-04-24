#! /bin/bash
fbm_files=$(find . -name "*.fbm" | cut -c 3-)
mkdir fbms
for fbm in ${fbm_files};do
  cp -a ${fbm} fbms/
done
