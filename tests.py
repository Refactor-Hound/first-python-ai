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
from functions.run_python_file import run_python_file

def demo():
  
    # print("Result for main.py:")
    # print(get_file_content("calculator", "main.py"))
    # print("Result for 'pkg/calculator.py' directory:")
    # print(get_file_content("calculator", "pkg/calculator.py"))
    # print("Result for '/bin/cat' directory:")
    # print(get_file_content("calculator", "/bin/cat"))
    # print("Result for non-exist file:")
    # print(get_file_content("calculator", "pkg/this_does_not_exist.py"))

    # print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
    # print(write_file("calculator", "pkg/morelorem.txt", "lorel upsum dolor sit amet"))
    # print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))


    print(run_python_file("calculator", "main.py"))
    print(run_python_file("calculator", "main.py", ["3 + 5"]))
    print(run_python_file("calculator", "tests.py"))
    print(run_python_file("calculator", "../main.py"))
    print(run_python_file("calculator", "nonexistent.py"))
    print(run_python_file("calculator", "lorem.txt"))


if __name__ == "__main__":
    demo()