from decompressor import Decompressor


class Checker:
    @staticmethod
    def check_member_header(
            decompressor: Decompressor
    ) -> (bool, str):
        raise NotImplementedError()

    @staticmethod
    def check_member_trailer(
            decompressor: Decompressor
    ) -> (bool, str):
        raise NotImplementedError()
