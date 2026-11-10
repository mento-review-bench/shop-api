import os

BASE = "/srv/uploads"

def read_upload(name):
    path = os.path.join(BASE, name)
    with open(path, "rb") as f:
        return f.read()
