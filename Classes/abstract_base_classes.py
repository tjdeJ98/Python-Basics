# reading data for a file is different from reading data from a network
# We want to create an abstract class, so we can't call it
from abc import ABC, abstractmethod


class InvalidOperationError(Exception):
    pass

# ABC makes is abstract, now All sub classes have a contract that when they inherit the class
# They have to implement the @abstractmethod methods before being able to be used.
# And the base Stream class can't be made anymore, only the sub classes


class Stream(ABC):
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already open.")
        self.opened = True

    def close(self):
        if not self.open:
            raise InvalidOperationError("Stream is already closed")
        self.opened = False

    @abstractmethod
    def read(self):
        pass


class FileStream(Stream):
    def read(self):
        print("Reading data from a file")


class NetworkStream(Stream):
    def read(self):
        print("Reading data from a network")

# Now it HAS to implement the read method!
# class MemoryStream(Stream):
#     pass
# SO:


class MemoryStream(Stream):
    def read(self):
        print("Reading data from a memory stream")


# This is an abstract concept: What are we working with? What kind of stream? File? Network?
# So we shouldn't be able to create a stream instance. But only the sub classes
# stream = Stream()

stream = MemoryStream()
stream.open()
