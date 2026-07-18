from pathlib import Path

path=Path("C:/Users/Rajasekar/OneDrive/_12_DATA_ANALYST/_08_libaries")
print(path.exists)
print(path.is_file())
print(path.is_dir())
print(path.name)
print(path.stem)
print(path.suffix)
print(path.parent)
print(path.anchor)
# print(path.parents)
for x in path.parents:
    print(x)
p=path.with_name(("_03_dir"))
print(p.absolute())


