import argparse
from os.path import isfile, splitext


def main():
    parser = argparse.ArgumentParser(description="Deflate")
    parser.add_argument(
        "path", type=str,
        help="Absolute path to a file to be (de)compressed",
    )
    parser.add_argument(
        "action", type=str,
        choices=["compress", "decompress"],
        help="Whether to compress or decompress given file"
    )
    args = parser.parse_args()
    if path_correct(args.path):
        pass
    else:
        raise AttributeError(f"Incorrect path: {args.path}")


def path_correct(path):
    if isfile(path):
        if splitext(path)[-1] != ".gz":
            print("A file must have a .gz extension")
            return False
        return True
    print("The path must lead to an existing .gz file")
    return False


if __name__ == "__main__":
    main()
