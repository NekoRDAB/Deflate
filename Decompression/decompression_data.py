from typing import List


class DecompressionData:
    def __init__(
            self,
            buf, buf_len, buf_pos, byte_pos,
            back_refs, back_refs_pos, back_refs_filled,
            out_buf, out_pos, f
    ):
        self.buf = buf
        self.buf_len = buf_len
        self.buf_pos = buf_pos
        self.byte_pos = byte_pos
        self.back_refs = back_refs
        self.back_refs_pos = back_refs_pos
        self.back_refs_filled = back_refs_filled
        self.out_buf = out_buf
        self.out_pos = out_pos
        self.f = f
