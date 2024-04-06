from pathlib import Path
from time import ctime
import shutil

source = Path(
    r"python standard library\working with directories\ecommerce\__init__.py")
target = Path(
    r"python standard library\working with directories") / "__init__.py"

# 2 ways of copying a file first is ofc better
shutil.copy(source, target)
target.write_text(source.read_text())


# path.exists()
# path.exists()
# path.rename("init.txt")
# path.unlink()
# print(ctime(path.stat().st_ctime))

# # path.read_bytes()
# print(path.read_text())
# path.write_text("....")
# path.write_bytes()
