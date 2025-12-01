import os
from google.genai import types

def get_files_info(working_directory, directory="."):
    candidate = os.path.join(working_directory, directory)
    base_abs = os.path.abspath(working_directory)
    cand_abs = os.path.abspath(candidate)

    if not (cand_abs == base_abs or cand_abs.startswith(base_abs + os.sep)):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
   
    if not os.path.isdir(cand_abs):
      return f'Error: "{directory}" is not a directory'

    try:
        entries = os.listdir(cand_abs)
        lines = []
        for entry in sorted(entries):
            full_path = os.path.join(cand_abs, entry)
            is_dir = os.path.isdir(full_path)
            size = os.path.getsize(full_path)
            lines.append(f"- {entry}: file_size={size} bytes, is_dir={is_dir}")
        return "\n".join(lines)
    except Exception as e:
        return f"Error: {e}"



schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)



