class BlockType00Format:
    def __init__(self,
                 is_last, padding,
                 length, length_complement, data
                 ):
        self.is_last = is_last
        self.padding = padding
        self.length = length
        self.length_complement = length_complement
        self.data = data
