import sqlite3
import json
from pathlib import Path

# movies = json.loads(Path(
#     r"python standard library\working with a SQLite database\movies.json").read_text())

# with sqlite3.connect("python standard library\working with a SQLite database\db.sqlite3") as connection:
#     command = "INSERT OR IGNORE INTO Movies VALUES(?, ?, ?)"

#     for movie in movies:
#         connection.execute(command, tuple(movie.values()))
#     connection.commit()


with sqlite3.connect("python standard library\working with a SQLite database\db.sqlite3") as connection:
    command = "SELECT * FROM Movies"
    cursor = connection.execute(command)
    # for row in cursor:
    #     print(row)
    movies = cursor.fetchall()
    print(movies)
