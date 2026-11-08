import os
import subprocess


def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:

    try:
        abs_working_dir= os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(abs_working_dir, file_path))
# Will be True or False
        valid_target_dir = os.path.commonpath([abs_working_dir, target_dir]) == abs_working_dir

        if valid_target_dir==False:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if os.path.isfile(target_dir)==False:
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'
        command=["python",target_dir]
        if args:
            command.extend(args)
        result=subprocess.run(command,cwd=abs_working_dir,capture_output=True,text=True,timeout=30,)
        messages=[]
        if result.returncode!=0:
            messages.append(f"Process exited with code {result.returncode}")
        if not result.stdout and not result.stderr:
            messages.append("No output produced")
        else:
            if result.stdout:
                messages.append(f'STDOUT: {result.stdout}')
            if result.stderr:
                messages.append(f'STDERR: {result.stderr}')

        final_output = "\n".join(messages)
        return final_output
    except Exception as e:
        return f"Error: executing Python file: {e}"

schema_run_python_file = {
    "type": "function",
        "function": {
            "name": "run_python_file",
            "description": "executes the file and returns its output in the working directory   ",
            "parameters": {
                "type": "object",
                "properties": {
                "file_path": {
                "type": "string",
                "description": "location of python file relative to the working directory ",
                    },
                "args":{
                "type": "array",
                "items":{"type":"string",
                        },
                "description": "Arguments for the Python file"
                    },
                },
                "required":["file_path"],
            },
        },
    }
