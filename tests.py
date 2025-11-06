# import unittest
# from functions.get_files_info import get_files_info

# class TestGetFilesInfo(unittest.TestCase):
#     def test_current_dir_lists_files(self):
#         result = get_files_info("calculator", ".")
#         self.assertIn("main.py", result)
#         self.assertIn("tests.py", result)
#         self.assertIn("pkg", result)
#         self.assertIn("is_dir=False", result)
#         self.assertIn("is_dir=True", result)
#         self.assertIn("file_size=", result)

#     def test_pkg_dir_lists_files(self):
#         result = get_files_info("calculator", "pkg")
#         self.assertIn("calculator.py", result)
#         self.assertIn("render.py", result)

#     def test_outside_dir_error(self):
#         result = get_files_info("calculator", "/bin")
#         self.assertIn("Error:", result)

#     def test_parent_escape_error(self):
#         result = get_files_info("calculator", "../")
#         self.assertIn("Error:", result)

#     def demo():
#         print("Result for current directory:")
#         print(get_files_info("calculator", "."))
#         print("Result for 'pkg' directory:")
#         print(get_files_info("calculator", "pkg"))
#         print("Result for '/bin' directory:")
#         print(get_files_info("calculator", "/bin"))
#         print("Result for '../' directory:")
#         print(get_files_info("calculator", "../"))

# if __name__ == "__main__":
#   unittest.main(), 



# JUST TO PASS THE SPECIFIC COURSE REQUIREMENTS
from functions.get_file_content import get_file_content

def demo():
    # print("Result for lorem:")
    # print(get_file_content("calculator", "lorem.txt"))

    print("Result for main.py:")
    print(get_file_content("calculator", "main.py"))
    print("Result for 'pkg/calculator.py' directory:")
    print(get_file_content("calculator", "pkg/calculator.py"))
    print("Result for '/bin/cat' directory:")
    print(get_file_content("calculator", "/bin/cat"))
    print("Result for non-exist file:")
    print(get_file_content("calculator", "pkg/this_does_not_exist.py"))

if __name__ == "__main__":
    demo()