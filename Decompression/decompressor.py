class Decompressor:
    def __init__(self, buf, buf_len, f):
        self._buf = buf
        self._buf_len = buf_len
        self._f = f
        self._buf_pos = 0

    def decompress_member(self) -> bool:
        while True:
            success, message = self.check_member_header()
            if not success:
                raise AttributeError(message)

            success, message = self.decompress_blocks()
            if not success:
                raise AttributeError("Failed to ")

    def check_member_header(self):
        pass

    def decompress_blocks(self):
        pass
