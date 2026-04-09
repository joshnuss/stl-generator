import os
import cadquery as cq
from tempfile import mkstemp


def export(object):
    (_, file) = mkstemp(suffix=".stl")
    data = None

    cq.exporters.export(object, file)

    with open(file, mode="rb") as f:
        data = f.read()

    os.remove(file)

    return data
