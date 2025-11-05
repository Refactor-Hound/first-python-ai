# import unittest
# from functions.get_files_info import get_files_info


# class TestSomething(unittest.TestCase):
#     def all_test(self):
#         result = get_files_info("calculator", ".")
#         self.assertIn(" - main.py: file_size=719 bytes, is_dir=False
# ", result)
#         self.assertIn(" - tests.py: file_size=1331 bytes, is_dir=False
# ", result)
#         self.assertIn(" - pkg: file_size=44 bytes, is_dir=True
# ", result)

#     def test_error_case(self):
#         result = some_function("bad_input")
#         self.assertIn("Error:", result)

#     def test_specific_subpath(self):
#         result = some_function("base", "subdir")
#         self.assertIn("subdir_name_or_file", result)
#         self.assertIn("is_dir=", result)

# if __name__ == "__main__":
#     unittest.main()


# python
import unittest
from functions.get_files_info import get_files_info

class TestGetFilesInfo(unittest.TestCase):
    def test_current_dir_lists_files(self):
        result = get_files_info("calculator", ".")
        self.assertIn("main.py", result)
        self.assertIn("tests.py", result)
        self.assertIn("pkg", result)
        self.assertIn("is_dir=False", result)
        self.assertIn("is_dir=True", result)
        self.assertIn("file_size=", result)

    def test_pkg_dir_lists_files(self):
        result = get_files_info("calculator", "pkg")
        self.assertIn("calculator.py", result)
        self.assertIn("render.py", result)

    def test_outside_dir_error(self):
        result = get_files_info("calculator", "/bin")
        self.assertIn("Error:", result)

    def test_parent_escape_error(self):
        result = get_files_info("calculator", "../")
        self.assertIn("Error:", result)

if __name__ == "__main__":
    unittest.main()