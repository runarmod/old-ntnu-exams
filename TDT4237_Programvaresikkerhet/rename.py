import os
import re
from itertools import groupby

for name, files in groupby(
    filter(lambda s: s.endswith(".pdf"), os.listdir(".")),
    lambda s: re.search(re.compile(r"\d{4}[VHK]"), s).group(0),
):
    os.makedirs(name, exist_ok=True)
    for file in files:
        os.rename(file, os.path.join(name, file))
