from contextlib import suppress
import os
import re

pattern = re.compile(r"^Matte4D-(\d+)((?:H)|(?:Kont))-?(.*)")

for file in os.listdir("."):
    match = re.match(pattern, file)
    if not match:
        continue
    year, _type, rest = match.groups()
    if rest == ".pdf":
        rest = "exam.pdf"
    print(f"{year}_{_type}/{rest}")
    # Move to year_type/rest
    with suppress(FileExistsError):
        os.mkdir(f"{year}_{_type}")
    os.rename(file, f"{year}_{_type}/{rest}")
