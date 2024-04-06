from pathlib import Path
from zipfile import ZipFile

# Will create this zip file to our current folder
target_folder = Path(
    r"python standard library\working with zip files\ecommerce")
# with ZipFile("files.zip", "w") as zip:
#     if target_folder.exists():
#         for path in target_folder.rglob("*.*"):
#             zip.write(path)

with ZipFile(r"python standard library\working with zip files\files.zip") as zip:
    print(zip.namelist())
    info = zip.getinfo(
        "ecommerce/__init__.py")
    print(info.file_size)
    print(info.compress_size)
    zip.extractall("extract")
