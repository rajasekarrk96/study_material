import json
from pathlib import Path

movies=[
    {"id":1, "title":"leo","year":2023},
    {"id":2, "title":"goat","year":2024},
]

d=json.dumps(movies)
print(d)

Path("movies.json").write_text(d)


d=Path("movies.json").read_text()
print(d,type(d))
d=json.loads(d)
print(d,type(d))