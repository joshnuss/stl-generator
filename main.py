import cadquery as cq
import stl

from microdot import Microdot

app = Microdot()


@app.route("/example.stl")
async def example(request):
    height = int(request.args.get("height", 10))
    radius = int(request.args.get("radius", 3))

    object = cq.Workplane("XY").cylinder(height, radius)

    data = stl.export(object)

    return data, {"content-type": "model/stl"}


app.run(debug=True)
