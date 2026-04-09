Parametric CAD model to STL
---------------------

This is a web app that returns a dynamically generated STL file based on a parametric CAD model.

The CAD model is defined using [cadquery](https://github.com/cadquery/cadquery) and served using [Microdot](https://github.com/miguelgrinberg/microdot).

## Usage

Download this repo:

```
gh repo clone joshnuss/stl-generator
```

Run the app:

```sh
python main.py
```

Visit the app in your browser:

```
http://localhost:5000/example.stl?height=100&radius=20
```

## License

MIT
