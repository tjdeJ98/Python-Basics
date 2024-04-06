# Datastructures like: list, sets, dicts, etc..., also known as ContainerTypes
# Sometimes we want to create our own ContainerTypes

# So let's make: a class that can keep track of the number of various tags that are on a block
# For example how many articels do we have that are tagged with python, javascript, etc..

# We can make this class a bit smarted then the standart dictonary we use.
# For example: Here we make it so our TagCloud is not case sensitive, which a dict would be
# Or we make it so that we can get the item just by tag, which we can't do in a dictonary.
class TagCloud:
    def __init__(self):
        # If we prefix a attribute with a double underscore "__" it makes it private to the class
        self.__tags = {}

    def add(self, tag):
        # get the tag or return 0 as a default value
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)

    def __setitem__(self, tag, number):
        self.__tags[tag.lower()] = number

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        # An iterator object is an object that walks over a container and gets one item at a time
        return iter(self.__tags)


cloud = TagCloud()
# attribute that holds all the attributes of a class so __tag is still accessable
print(cloud.__dict__)
# So we can always access then, just note that it is a warning to the consumer that this shouldn't be accessed
print(cloud._TagCloud__tags)
cloud.add("python")
# We shouldn't have access to the underlying tags object. So we always need to use the other options
# print(cloud.tags["PYTHON"])
