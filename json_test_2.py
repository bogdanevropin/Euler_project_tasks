import json
from pathlib import Path

data = Path("movies.json").read_text()
movies = json.loads(data)
print(movies)
print(movies[0]["title"])