# reading data for a file is different from reading data from a network
class InvalidOperationError(Exception):
    pass


class Stream:
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


class FileStream(Stream):
    def read(self):
        print("Reading data from a file")


class NetworkStream(Stream):
    def read(self):
        print("Reading data from a network")


# This is an abstract concept: What are we working with? What kind of stream? File? Network?
# So we shouldn't be able to create a stream instance. But only the sub classes
stream = Stream()
stream.open()
