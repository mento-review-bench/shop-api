import os

BASE = "/srv/uploads"

def read_upload(name):
    path = os.path.realpath(os.path.join(BASE, name))
    if not path.startswith(BASE + os.sep):
        raise ValueError("bad path")
    with open(path, "rb") as f:
        return f.read()
