# BTB-Tool-Templates

The purpose of this is to create a museum structure of various models for Godot. This is done through multiple steps.

1. Coversion - All 3d file types are converted to obj and all texture types are converted to normal and diffuse png textures. If normal files do not exist they are created.
2. Resizing - All image files are converted to a smaller standard image size.
3. Rotating - Given a preset rotation value or map of values, the program will rotate some or all models to a specific position.
4. Templating - Jinja2 templates are used to describe material and scenes of each model. Godot code is also generated so that museum can be loaded.

## Future Work
- Handle multimesh models and mulitple texture models - likely to be used for specific models or sets, possible specialized map solution.
- Splicer splits models into specific pieces. i.e head, shoulder, feet etc.
- Auto texture manipulation - each diffuse texture becomes multiple color and tone variations - and/or handling of existing color alternates