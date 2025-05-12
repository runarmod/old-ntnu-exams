import os
from itertools import groupby
import re

pattern = re.compile(r"\d{4}[VK]")

for name, files in groupby(
    filter(lambda s: re.search(pattern, s), os.listdir(".")),
    lambda s: re.search(pattern, s).group(0),
):
    os.makedirs(name, exist_ok=True)
    for file in files:
        os.rename(file, os.path.join(name, file))
