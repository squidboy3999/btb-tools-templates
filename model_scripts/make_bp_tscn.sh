#! /bin/bash
body_path=000_static_body_parts_x-bot
mat=000_materials
for body_part in $(ls $body_path);do
echo "... working on ${body_part}  ..."
is_mat_dir=$(echo $body_part|grep 000_materials| wc -l)
is_finger_dir=$(echo $body_part|grep fingers| wc -l)
if [ $is_mat_dir -lt 1 ];then
if [ $is_finger_dir -lt 1 ];then
for letter in $(ls $body_path/$body_part);do
echo "... working on ${body_part}\/${letter}  ..."
is_template=$(echo $letter|grep 0_template_xbot| wc -l)
if [ $is_template -lt 1 ];then
for model_dir in $(ls $body_path/$body_part/$letter);do
echo "... working on ${body_part}\/${letter}\/${model_dir}  ..."
tscn_present=$(ls $body_path/$body_part/$letter/$model_dir | grep .tscn| wc -l)
if [ $tscn_present -lt 1 ];then
cp ${body_path}/${body_part}/0_template_xbot/0_script_template_xbot.tscn ${body_path}/${body_part}/${letter}/${model_dir}/${model_dir}.tscn
character=$(echo $model_dir|cut -d "_" -f 1)
lower_char=$(echo $character | awk '{print tolower($0)}')
game=$(echo $model_dir|cut -d "_" -f 2)
museum=$game
if [ $(echo $game|grep GhostbustersWorld| wc -l) -gt 0 ];then
museum=Ghostbusters
fi
mat_dir="${character}_${museum}"
echo "--- LETTERVAL=${letter} ---"
echo "--- NAMELOWER=${lower_char} ---"
echo "--- NAMEUPPER_OBJDIR=${model_dir} ---"
echo "--- NAMEUPPER_MATDIR=${mat_dir} ---"
sed -i "s/LETTERVAL/${letter}/g" ${body_path}/${body_part}/${letter}/${model_dir}/${model_dir}.tscn
sed -i "s/NAMELOWER/${lower_char}/g" ${body_path}/${body_part}/${letter}/${model_dir}/${model_dir}.tscn
sed -i "s/NAMEUPPER_OBJDIR/${model_dir}/g" ${body_path}/${body_part}/${letter}/${model_dir}/${model_dir}.tscn
sed -i "s/NAMEUPPER_MATDIR/${mat_dir}/g" ${body_path}/${body_part}/${letter}/${model_dir}/${model_dir}.tscn
fi
done
fi
done
fi
fi
done
