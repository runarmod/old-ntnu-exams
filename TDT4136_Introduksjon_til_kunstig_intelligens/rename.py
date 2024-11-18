import os
import re

pattern = re.compile(r"^exam(\d+)((?:ord)|(?:test)|(?:kont))_(.*)")

for file in os.listdir("."):
    match = re.match(pattern, file)
    if not match:
        continue
    year, _type, rest = match.groups()
    print(year, _type, rest)
    # Move to year_type/rest
    try:
        os.mkdir(f"{year}_{_type}")
    except FileExistsError:
        pass
    os.rename(file, f"{year}_{_type}/{rest}")
