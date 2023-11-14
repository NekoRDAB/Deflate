from bit_stream_reader import BitStreamReader
import BlockTypes.blocktype_format as bformat


class CompressedBlockParser:
    @staticmethod
    def parse_block(bit_stream: BitStreamReader) -> bformat.BlockFormat:
        is_last = bit_stream.next_bit()
        btype = bit_stream.next_bits(2)
        body = CompressedBlockParser.parse_body(btype, bit_stream)
        return bformat.BlockFormat.create_block(is_last, btype, body)

    @staticmethod
    def parse_body(btype: str, bit_stream: BitStreamReader):
        raise NotImplementedError()
