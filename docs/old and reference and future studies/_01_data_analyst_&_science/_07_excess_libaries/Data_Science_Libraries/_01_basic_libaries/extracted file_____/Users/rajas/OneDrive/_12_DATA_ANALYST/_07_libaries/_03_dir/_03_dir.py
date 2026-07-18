from pathlib import Path

path=Path("/_08_libaries/_01_basic_libaries/_03_dir")
print(path.iterdir())
for x in path.iterdir():
    print(x)

paths=[p for p in path.iterdir() if p.is_dir()]
print(paths)
print([p for p in (path.glob("*.py"))])
print(path.exists())
# path.mkdir()
# path.rmdir()
# path.rename("check")
