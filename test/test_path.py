import unittest
from main import path_correct


PATH_TO_DIR = "D:\\GitHubProjects\\Deflate\\test\\text_files\\files_path\\"


class TestPath(unittest.TestCase):
    def test_correct_path(self):
        self.assertTrue(path_correct(PATH_TO_DIR + "correct_extension.gz"))
        self.assertFalse(path_correct("not_existing_file.gz"))
        self.assertFalse(path_correct(PATH_TO_DIR + "incorrect_extension.txt"))


if __name__ == '__main__':
    unittest.main()
