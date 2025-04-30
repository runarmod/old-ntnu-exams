import os
from itertools import groupby

for name, files in groupby(
    filter(lambda s: s.endswith(".pdf"), os.listdir(".")), lambda s: s[:5]
):
    os.makedirs(name, exist_ok=True)
    for file in files:
        os.rename(file, os.path.join(name, file))
