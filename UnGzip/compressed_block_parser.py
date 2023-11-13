from bit_stream_reader import BitStreamReader


class CompressedBlockFormat:
    def __init__(self, is_last: str, btype: str, block_body: str):
        self.is_last = is_last
        self.btype = btype
        self.block_body = block_body


class CompressedBlockParser:
    @staticmethod
    def parse_block(bit_stream: BitStreamReader) -> CompressedBlockFormat:
        is_last = bit_stream.next_bit()
        btype = bit_stream.next_bits(2)
        data = CompressedBlockParser.parse_data(btype, bit_stream)
        return CompressedBlockFormat(is_last, btype, data)

    @staticmethod
    def parse_data(btype: str, bit_stream: BitStreamReader) -> str:
        raise NotImplementedError()
