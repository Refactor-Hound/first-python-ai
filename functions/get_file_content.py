import os
from config import MAX_CHARS
from google.genai import types


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



schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Reading file contents and caps the content at 10000 characters, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path to read contents from, relative to the working directory. If longer than 10000 characters, it caps it and adds a notice in a string.",
            ),
        },
    ),
)