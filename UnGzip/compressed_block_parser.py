from bit_stream_reader import BitStreamReader


class BlockFormat:
    def __init(self, is_last: str, btype: str, data: str):
        self.is_last = is_last
        self.btype = btype
        self.data = data


class CompressedBlockParser:
    @staticmethod
    def parse_block(bit_stream: BitStreamReader):
        raise NotImplementedError()
