cd ..
docker run -d -v /model_files --name pt_maker png_tscn_maker
docker cp model_files pt_maker:/
docker cp rename_dict.json pt_maker:/
docker exec -it pt_maker sh -c "python3 /usr/local/lib/python3.7/site-packages/btb_tools_templates/image_converter.py /model_files/"
docker cp pt_maker:/var/log/image_converter.log model_files/
docker cp pt_maker:/model_files model_files/done
cd btb-tools-templates