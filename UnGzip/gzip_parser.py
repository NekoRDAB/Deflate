from bit_stream_reader import BitStreamReader
from compressed_block_parser import CompressedBlockParser, CompressedBlockFormat


class GzipFormat:
    def __init__(self, header: dict, compressed_blocks: list, footer: dict):
        self.header = header
        self.compressed_blocks = compressed_blocks
        self.footer = footer


class GzipParser:
    @staticmethod
    def parse_bit_stream(bit_stream: BitStreamReader) -> GzipFormat:
        header = GzipParser.parse_header(bit_stream)
        compressed_blocks = GzipParser.parse_compressed_blocks(bit_stream)
        footer = GzipParser.parse_footer(bit_stream)
        return GzipFormat(header, compressed_blocks, footer)

    @staticmethod
    def parse_header(bit_stream: BitStreamReader) -> dict:
        header = {
            "id1": bit_stream.next_byte(),
            "id2": bit_stream.next_byte(),
            "compression_method": bit_stream.next_byte(),
            "flags": bit_stream.next_byte(),
            "mtime": bit_stream.next_bytes(4),
            "xfl": bit_stream.next_byte(),
            "os": bit_stream.next_byte(),
        }
        return header

    @staticmethod
    def parse_compressed_blocks(bit_stream: BitStreamReader) -> list:
        blocks = []
        block = GzipParser.parse_compressed_block(bit_stream)
        blocks.append(block)
        while not block.is_last:
            block = GzipParser.parse_compressed_block(bit_stream)
            blocks.append(block)
        return blocks

    @staticmethod
    def parse_compressed_block(bit_stream: BitStreamReader) -> CompressedBlockFormat:
        raise NotImplementedError()

    @staticmethod
    def parse_footer(bit_stream: BitStreamReader) -> dict:
        footer = {
            "crc32": bit_stream.next_bytes(4),
            "isize": bit_stream.next_bytes(4),
        }
        return footer
