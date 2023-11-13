import bitstring


class BinaryReader:
    def __init__(self, data: str):
        self._data = data
        self._ptr: int = 0

    @staticmethod
    def read_file(path: str):
        with open(path, "rb") as file:
            data = bitstring.Bits(file).bin
        return BinaryReader(data)

    def next_bit(self) -> str:
        if self._ptr >= len(self._data):
            raise IndexError("Pointer out of range")
        result = self._data[self._ptr]
        self._ptr += 1
        return result

    def next_byte(self) -> str:
        return "".join([self.next_bit() for _ in range(8)])

    @property
    def data(self):
        return self._data

    @property
    def pointer(self):
        return self._ptr
