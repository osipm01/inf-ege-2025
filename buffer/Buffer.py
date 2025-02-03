import sys

from BufferUtiles import BufferUtiles

class Buffer_R2:
    def __init__(self, data):
        self.buffer2 = []
        self.data = data
        self.tools = BufferUtiles()
        self.return_value = None

    # buffer initialization
    def create_buffer2r(self):
        if len(self.data) != 2:
            print("error of init buffer => buffer size <2 use buffer 3")
            sys.exit(-1)
        self.buffer2 = self.data

    # get value from buffer
    def get_value_from_buffer(self):
        self.return_value = self.buffer2[0]
        self.buffer2[0] = self.buffer2[1]
        return self.return_value

    # set value to buffer by id
    def set_value_to_buffer(self, id, data=None):
        if data is not None:
            self.buffer2[id] = data

    # set next value to buffer
    def set_next_value_to_buffer(self, NextData):
        self.buffer2[len(self.buffer2) - 1] = NextData
