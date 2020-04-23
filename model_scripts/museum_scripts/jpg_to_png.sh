#! /bin/bash
for dir in $(ls);do
pushd ${dir}
find . -name "*.jpg" -exec mogrify -format png {} \;
find . -name "*.jpeg" -exec mogrify -format png {} \;
rm *.jpg
rm *.jpeg
popd
done
