class BufferEmptyException(Exception):
    pass


class BufferFullException(Exception):
    pass


class CircularBuffer:
    def __init__(self, size):
        if not isinstance(size, int) and size < 1:
            raise ValueError("You entered invalid size of the buffer")
        self.size, self.pos_read, self.pos_write = size, 0, 0
        self.buffer = [None for _ in range(size)]

    def read(self):
        if self.buffer[self.pos_read] is None:
            raise BufferEmptyException("Buffer is empty")
        output = self.buffer[self.pos_read]
        self.buffer[self.pos_read] = None
        self.pos_read = (self.pos_read + 1) % self.size
        return output

    def write(self, value):
        if self.buffer[self.pos_write] is not None:
            raise BufferFullException("Buffer is full")
        self.buffer[self.pos_write] = value
        self.pos_write = (self.pos_write + 1) % self.size

    def overwrite(self, value):
        if self.buffer[self.pos_write] is not None:
            self.pos_read = (self.pos_read + 1) % self.size
        self.buffer[self.pos_write] = value
        self.pos_write = (self.pos_write + 1) % self.size

    def clear(self):
        self.__init__(self.size)
