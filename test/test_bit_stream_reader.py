import unittest
from bit_stream_reader import BitStreamReader


PATH = "D:\\GitHubProjects\\Deflate\\test\\text_files\\files_binary_reader\\hello_world.txt"


class TestBitStreamReader(unittest.TestCase):
    def test_init(self):
        bit_stream_reader = BitStreamReader.read_file(PATH)
        expected = ("0100100001100101011011000110110001101111001011"
                    "00001000000101011101101111011100100110110001100"
                    "10000100001")
        actual = bit_stream_reader.data
        self.assertEqual(expected, actual)
        self.assertEqual(0, bit_stream_reader.pointer)

    def test_next_bit(self):
        bit_stream_reader = BitStreamReader.read_file(PATH)
        expected = "01001000"
        actual = "".join([bit_stream_reader.next_bit() for _ in range(8)])
        self.assertEqual(expected, actual)

    def test_next_byte(self):
        bit_stream_reader = BitStreamReader.read_file(PATH)
        expected = "0100100001100101"
        actual = bit_stream_reader.next_bytes(2)
        self.assertEqual(expected, actual)

    def test_out_of_range(self):
        bit_stream_reader = BitStreamReader.read_file(PATH)
        data = bit_stream_reader.data
        for i in range(len(data)):
            bit_stream_reader.next_bit()
        self.assertRaises(IndexError, bit_stream_reader.next_bit)

    def test_pointer(self):
        bit_stream_reader = BitStreamReader.read_file(PATH)
        for _ in range(8):
            bit_stream_reader.next_bit()
        bit_stream_reader.next_byte()
        expected = 16
        actual = bit_stream_reader.pointer
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
