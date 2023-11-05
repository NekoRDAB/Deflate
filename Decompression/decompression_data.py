class DecompressionData:
    def __init__(
            self,
            bitstream, bs_length, bs_pos, byte_pos,
            back_refs, back_refs_pos, back_refs_filled,
            output, output_pos, output_file_stream
    ):
        self.bitstream = bitstream
        self.bs_length = bs_length
        self.bs_pos = bs_pos
        self.byte_pos = byte_pos
        self.back_refs = back_refs
        self.back_refs_pos = back_refs_pos
        self.back_refs_filled = back_refs_filled
        self.output = output
        self.output_pos = output_pos
        self.output_file_stream = output_file_stream
