from pathlib import Path

path = Path("Euler/__init__.py")
path.exists()
path.is_file()

print(path.name)
print(path.parent)
print(path.suffix)

path1 = path.with_name("names.txt")
path2 = path.with_suffix(".txt")
print(path.absolute())

path = [p for p in path.iterdir() if p.is_dir()]
print(path)