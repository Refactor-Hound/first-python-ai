import subprocess
import os
import sys
python_exe = sys.executable



def run_python_file(working_directory, file_path, args=[]):
    abs_base = os.path.abspath(working_directory)
    abs_target = os.path.abspath(os.path.join(abs_base, file_path))

    base_with_sep = abs_base if abs_base.endswith(os.sep) else abs_base + os.sep


    if not abs_target.startswith(base_with_sep):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    if not os.path.exists(abs_target):
      return f'Error: File "{file_path}" not found.'

    if not abs_target.endswith(".py"):
      return f'Error: "{file_path}" is not a Python file.'
    

    try:
      result = subprocess.run([python_exe, abs_target, *args], timeout=30, capture_output=True, text=True, cwd=abs_base)
      if not result.stdout and not result.stderr:
        return 'No output produced.'
      if result.returncode != 0:
        return f'STDOUT:{result.stdout}\nSTDERR:{result.stderr}\nProcess exited with code {result.returncode}'
      else:
        return f'STDOUT:{result.stdout}\nSTDERR:{result.stderr}'
    except Exception as e:
      return f"Error: executing Python file: {e}"
