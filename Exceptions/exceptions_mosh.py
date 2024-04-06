try:
    # When opened in this way the file will automatically be closed at the end
    # Python automaticilly calls: .__enter__ and .__exit__ (Magic Classes)
    with open("app.py") as file:  # , open("another.txt") as target:
        print("File opened")
        file.__exit
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")
else:
    print("No exceptions were thrown.")
