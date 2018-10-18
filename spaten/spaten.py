from .fileformat_pb2 import Body

from shapely.wkb import loads


BYTEORDER = 'little'


class SpatenFile(object):
    def __init__(self, f):
        self.f = f

    def __enter__(self):
        if isinstance(self.f, str):
            self.r = open(self.f, 'rb')
        self.read_header()
        return self

    def __exit__(self, *args, **kwargs):
        if hasattr(self.r, 'close'):
            self.r.close()

    def read(self, size):
        """Reads the specified number of bytes and checks if EOF has occured"""
        buf = self.r.read(size)
        if len(buf) != size:
            raise EOFError
        return buf

    def read_int(self, size):
        return int.from_bytes(self.read(size), BYTEORDER)

    def read_header(self):
        cookie = self.r.read(4)
        if cookie != b'SPAT':
            raise ValueError('Invalid header')
        version = int.from_bytes(self.r.read(4), BYTEORDER)
        if version != 0:
            raise ValueError('The library only supports Spaten version 0')
        return version

    def read_block(self):
        body_len = self.read_int(4)
        flags = self.read_int(2)
        compression = self.read_int(1)
        message_serialization = self.read_int(1)

        if compression != 0:
            raise AttributeError('compression in Spaten files not supported by library')

        if message_serialization != 0:
            raise AttributeError('non-protobuf Spaten files are not supported')

        bodybuf = self.read(body_len)
        body = Body()
        body.ParseFromString(bodybuf)
        return body

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return self.read_block()
        except EOFError:
            raise StopIteration


def read(f):
    return SpatenFile(f)
