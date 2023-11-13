import bitstring


class BinaryReader:
    def __init__(self, path: str):
        with open(path, "rb") as file:
            self._data = bitstring.Bits(file).bin
        self._pointer: int = 0

    def next_bit(self) -> str:
        if self._pointer >= len(self._data):
            raise IndexError("Pointer out of range")
        result = self._data[self._pointer]
        self._pointer += 1
        return result

    def next_byte(self) -> str:
        return "".join([self.next_bit() for _ in range(8)])

    @property
    def data(self):
        return self._data
