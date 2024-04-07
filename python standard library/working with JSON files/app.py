import json
from pathlib import Path

# movies = [
#     dict(id=1, title="Terminator", year=1989),
#     dict(id=1, title="Kindergarten", year=1993)
# ]

# data = json.dumps(movies)

# Path("movies.json").write_text(data)
data = Path(
    r"python standard library\working with JSON files\movies.json").read_text()
movies = json.loads(data)
print(movies[0]["title"])
