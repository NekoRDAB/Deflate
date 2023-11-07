from error_handler import ErrorHandler
from checker import Checker


class Decompressor:
    def __init__(self, buf, buf_len, f):
        self._buf = buf
        self._buf_len = buf_len
        self._f = f
        self._buf_pos = 0

    def decompress_member(self) -> bool:
        while self._buf_pos < self._buf_len:
            success, message = Checker.check_member_header(self)
            if not success:
                ErrorHandler.throw_error(
                    AttributeError, message
                )

            success, message = self.decompress_blocks()
            if not success:
                ErrorHandler.throw_error(
                    AttributeError, message
                )

            success, message = Checker.check_member_trailer(self)
            if not success:
                ErrorHandler.throw_error(
                    AttributeError, message
                )

        return True

    def decompress_blocks(self) -> (bool, str):
        raise NotImplementedError()
