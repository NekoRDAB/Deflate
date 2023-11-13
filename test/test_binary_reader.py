import unittest
from binary_reader import BinaryReader


PATH = "D:\\GitHubProjects\\Deflate\\test\\text_files\\files_binary_reader\\hello_world.txt"


class TestBinaryReader(unittest.TestCase):
    def test_init(self):
        binary_reader = BinaryReader(PATH)
        expected = ("0100100001100101011011000110110001101111001011"
                    "00001000000101011101101111011100100110110001100"
                    "10000100001")
        actual = binary_reader.data
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
