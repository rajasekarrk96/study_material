from pathlib import Path
from zipfile import ZipFile

f=open("raj.txt","w")
f.write("raj")
f.close()

with open("raj.txt","r") as file:
    print(file.read())


with ZipFile("files.zip","w") as zip:
    p=Path("C:\\Users\\rajas\\OneDrive\\_12_DATA_ANALYST\\_08_libaries\\_03_dir")
    for path in p.rglob("*.*"):
        zip.write(path)
zip.close()

with ZipFile("files.zip") as zip:
    print(zip.namelist())
    zip.extractall("extracted file")
print('ok')