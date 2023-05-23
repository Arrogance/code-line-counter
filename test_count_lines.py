import os
import unittest
from count_lines import count_lines_of_code

class CodeLineCounterTests(unittest.TestCase):

    def setUp(self):
        self.project_directory = "test_project"
        self.excluded_folders = ["tests"]
        self.ignored_extensions = [".txt"]

    def test_line_count(self):
        expected_line_count = 10
        line_count = count_lines_of_code(self.project_directory, exclude_folders=self.excluded_folders, ignore_extensions=self.ignored_extensions)
        self.assertEqual(line_count, expected_line_count)

if __name__ == "__main__":
    unittest.main()
