import os




def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:
        abs_working_dir= os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(abs_working_dir, file_path))
    # Will be True or False
        valid_target_dir = os.path.commonpath([abs_working_dir, target_dir]) == abs_working_dir

        if valid_target_dir==False:
            return (f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory')
        if os.path.isdir(target_dir)==True:
            return f'Error: Cannot write to "{file_path}" as it is a directory'


        os.makedirs(os.path.dirname(target_dir),exist_ok=True)

        with open(target_dir ,"w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        return f"Error: {e}"


schema_write_file = {
    "type": "function",
        "function": {
            "name": "write_file",
            "description": "write_file  ",
            "parameters": {
                "type": "object",
                "properties": {
                "file_path": {
                "type": "string",
                "description": " path of file to write",
                    },
                "content":{
                "type": "string",
                "description": "content to write",
                    },
                },
                "required":["file_path","content"],
            },
        },
    }
