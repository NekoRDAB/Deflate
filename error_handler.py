class ErrorHandler:
    @staticmethod
    def throw_error(err, message: str = ""):
        print("An error occurred while decompressing:")
        raise err(message)
