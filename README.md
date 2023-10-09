# rye-sample

[Rye](https://github.com/mitsuhiko/rye) sample project

# sample

```bash
# create project
rye init rye_sample

# add package to project
rye add flask
rye add --dev black
rye sync # sync dev-dependency

# format by black
rye run black

# activate virtualenv
. .venv/bin/activate
```
