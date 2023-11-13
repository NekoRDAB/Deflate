import unittest
from binary_reader import BinaryReader


PATH = "D:\\GitHubProjects\\Deflate\\test\\text_files\\files_binary_reader\\hello_world.txt"


class TestBinaryReader(unittest.TestCase):
    def test_init(self):
        binary_reader = BinaryReader.read_file(PATH)
        expected = ("0100100001100101011011000110110001101111001011"
                    "00001000000101011101101111011100100110110001100"
                    "10000100001")
        actual = binary_reader.data
        self.assertEqual(expected, actual)
        self.assertEqual(0, binary_reader.pointer)

    def test_next_bit(self):
        binary_reader = BinaryReader.read_file(PATH)
        expected = "01001000"
        actual = "".join([binary_reader.next_bit() for _ in range(8)])
        self.assertEqual(expected, actual)

    def test_next_byte(self):
        binary_reader = BinaryReader.read_file(PATH)
        expected = "0100100001100101"
        actual = binary_reader.next_byte() + binary_reader.next_byte()
        self.assertEqual(expected, actual)

    def test_out_of_range(self):
        binary_reader = BinaryReader.read_file(PATH)
        data = binary_reader.data
        for i in range(len(data)):
            binary_reader.next_bit()
        self.assertRaises(IndexError, binary_reader.next_bit)

    def test_pointer(self):
        binary_reader = BinaryReader.read_file(PATH)
        for _ in range(8):
            binary_reader.next_bit()
        binary_reader.next_byte()
        expected = 16
        actual = binary_reader.pointer
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
