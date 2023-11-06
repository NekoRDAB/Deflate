import unittest
from Structures.value_and_bits import ValueAndBits, ValueAndBitsList


class TestValueAndBits(unittest.TestCase):
    def test_init(self):
        value_and_bits: ValueAndBits = ValueAndBits(1, 2)
        self.assertTrue(value_and_bits._value == 1 and value_and_bits._extra_bits == 2)

    def test_list_init(self):
        pairs = [(1, 2), (3, 4), (5, 6)]
        value_and_bits_list = ValueAndBitsList.create_list(*pairs)
        for i in range(len(pairs)):
            self.assertTrue(pairs[i][0] == value_and_bits_list[i]._value)
            self.assertTrue(pairs[i][1] == value_and_bits_list[i]._extra_bits)


if __name__ == '__main__':
    unittest.main()
