import sys

if len(sys.argv) == 1:
    print("USAGE: python3 app.py <password>")
else:
    password = sys.argv[1]
    print("Password", password)

# make sure you are in the right directory with command-line
# in command-line write: python3 app.py <anything>
