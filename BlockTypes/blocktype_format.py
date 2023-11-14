class BlockFormat:
    def __init__(self, is_last, btype):
        self.is_last = is_last
        self.btype = btype

    @staticmethod
    def create_block(is_last: str, btype: str, body: dict):
        if btype == "00":
            return BType00Format(is_last, *body)
        if btype == "01":
            return BType01Format(is_last, *body)
        if btype == "10":
            return BType10Format(is_last, *body)
        raise AttributeError(f"Unexpected btype: {btype}")


class BType00Format(BlockFormat):
    def __init__(self, is_last, padding, length, length_complement, data):
        super().__init__(is_last, "00")
        self.padding = padding
        self.length = length
        self.length_complement = length_complement
        self.data = data


class BType01Format(BlockFormat):
    raise NotImplementedError()


class BType10Format(BlockFormat):
    raise NotImplementedError()
