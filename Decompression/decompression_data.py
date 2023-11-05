from typing import List


class DecompressionData:
    def __init__(
            self,
            buf: List[int], buf_length, buf_pos, byte_pos,
            back_refs, back_refs_pos, back_refs_filled,
            output, output_pos, output_file_stream
    ):
        self.buf = buf
        self.buf_length = buf_length
        self.buf_pos = buf_pos
        self.byte_pos = byte_pos
        self.back_refs = back_refs
        self.back_refs_pos = back_refs_pos
        self.back_refs_filled = back_refs_filled
        self.output = output
        self.output_pos = output_pos
        self.output_file_stream = output_file_stream
