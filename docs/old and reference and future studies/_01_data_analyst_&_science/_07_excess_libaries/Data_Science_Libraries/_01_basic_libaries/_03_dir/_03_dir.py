from pathlib import Path

path=Path("C:/Users/Rajasekar/OneDrive/_12_DATA_ANALYST/_08_libaries")
print(path.exists())
print(path.iterdir())
for x in path.iterdir():
    print(x)

paths=[p for p in path.iterdir() if p.is_dir()]
print(paths)
print([p for p in (path.glob("*.py"))])

# path.mkdir()
# path.rmdir()
# path.rename("check")
