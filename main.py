import argparse
from os.path import isfile


def main():
    parser = argparse.ArgumentParser(description="Deflate")
    parser.add_argument(
        "path", type=str,
        help="Absolute path to a file to be compressed",
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
    return isfile(path)


if __name__ == "__main__":
    main()
