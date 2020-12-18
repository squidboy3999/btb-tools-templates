# BTB-Tool-Templates

The purpose of this is to create a museum structure of various models for Godot. This is done through multiple steps.

1. Coversion - All 3d file types are converted to obj and all texture types are converted to normal and diffuse png textures. If normal files do not exist they are created.
2. Resizing - All image files are converted to a smaller standard image size.
3. Rotating - Given a preset rotation value or map of values, the program will rotate some or all models to a specific position.
4. Templating - Jinja2 templates are used to describe material and scenes of each model. Godot code is also generated so that museum can be loaded.

## How to use
- To create a new docker image- in project directory:
  docker build --tag img-to-png .
  cd ..

- Run the container (issues seem to exist with volume mounts in windows, so perform a copy instead) - in directory with img_files in it.
  docker run -d --name i2p img-to-png
  docker cp img_files i2p:/
  docker exec -it i2p sh -c "python3 /usr/local/lib/python3.7/site-packages/btb_tools_templates/image_converter.py /img_files/"

- copy out png texture and normal files
  docker cp i2p:/img_files img_files/done


## Future Work
- Handle multimesh models and mulitple texture models - likely to be used for specific models or sets, possible specialized map solution.
- Splicer splits models into specific pieces. i.e head, shoulder, feet etc.
- Auto texture manipulation - each diffuse texture becomes multiple color and tone variations - and/or handling of existing color alternates