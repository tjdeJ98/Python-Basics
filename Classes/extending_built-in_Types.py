# This Text class now inherits all features from the str Class
# And we can add extra features to it.
class Text(str):
    def duplicate(self):
        return self + self


class TrackableList(list):
    # Here we are just extending the append method of the list class
    # We are not replacing it
    def append(self, object):
        print("Append called")
        super().append(object)


text = Text("Python")
# See how text has all methods of a str and the duplicate method
print(text.duplicate())
list = TrackableList()
list.append('1')
