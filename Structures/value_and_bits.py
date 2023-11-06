class ValueAndBits:
    def __init__(self, value, extra_bits):
        self._value = value
        self._extra_bits = extra_bits


class ValueAndBitsList:
    @staticmethod
    def create_list(*pairs):
        return [ValueAndBits(*pair) for pair in pairs]
