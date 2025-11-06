import os
from config.py import MAX_CHARS

def get_file_content(working_directory, file_path):
  abs_working_directory_nc = os.path.normcase(os.path.abspath(working_directory))
  abs_file_path_nc = os.path.normcase(os.path.abspath(os.path.join(working_directory,file_path)))
  
  working_directory_sep = abs_working_directory_nc if abs_working_directory_nc.endswith(os.sep) else abs_working_directory_nc + os.sep

  if not abs_file_path_nc.startswith(working_directory_sep):
    return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

  if not os.path.isfile(abs_file_path_nc):
    return f'Error: File not found or is not a regular file: "{file_path}"'

  try:
    with open(abs_file_path_nc, "r") as f:
      file_content_string = f.read(MAX_CHARS +1)
      if len(file_content_string) > MAX_CHARS:
        file_content_string = file_content_string[:MAX_CHARS] + f'[...File "{file_path}" truncated at 10000 characters]'
    return file_content_string
  
  except Exception as e:
    return f"Error: {e}"
