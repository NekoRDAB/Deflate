class BinaryConverter:
    TEXTCHARS = bytearray({7, 8, 9, 10, 12, 13, 27} | set(range(0x20, 0x100)) - {0x7f})

    @staticmethod
    def convert_to_binary(file):
        if BinaryConverter.is_binary_file(file):
            return file
        raise NotImplementedError

    @staticmethod
    def is_binary_file(path):
        with open(path, "rb") as file:
            byte_string = file.read(1024)
            return bool(byte_string.translate(None, BinaryConverter.TEXTCHARS))
