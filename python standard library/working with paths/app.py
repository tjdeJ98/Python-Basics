# The Path class: fountation to work with files and directories
from pathlib import Path
import ecommerce

print(ecommerce.__package__)
path = Path(r"python standard library\working with directories\ecommerce")

# print(path.is_file())
# print(path.is_dir())
# print(path.name)
# print(path.stem)
# print(path.suffix)
# print(path.parent)
# path = path.with_suffix(".txt")
# print(path)

paths = [p for p in path.iterdir() if p.is_dir()]
print(paths)
