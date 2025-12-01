import os
from google.genai import types


def write_file(working_directory, file_path, content):

    abs_base = os.path.abspath(working_directory)
    abs_target = os.path.abspath(os.path.join(abs_base, file_path))

    base_with_sep = abs_base if abs_base.endswith(os.sep) else abs_base + os.sep
    if not abs_target.startswith(base_with_sep):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    try:
        parent_dir = os.path.dirname(abs_target)
        if parent_dir and not os.path.exists(parent_dir):
            os.makedirs(parent_dir)

        with open(abs_target, "w") as f:
            f.write(content)

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: {e}"


# schema_write_file = types.FunctionDeclaration(
#     name="write_file",
#     description="Creates and writes to a new file.",
#     parameters=types.Schema(
#         type=types.Type.OBJECT,
#         properties={
#             "file_path": types.Schema(
#                 type=types.Type.STRING,
#                 description="The file path to write the file to."),
#             "content": types.Schema(
#         type=types.Type.STRING,
#         description="String to write to the file.")
#         }
#     )
# )
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Creates and writes to a new file.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path to write the file to.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="String to write to the file.",
            ),
        },
        required=["file_path", "content"],
    ),
)