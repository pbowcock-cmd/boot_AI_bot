import os





def get_file_content(working_directory: str, file_path: str) -> str:
    MAX_CHARS=10000
    try:
        abs_working_dir= os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(abs_working_dir, file_path))
    # Will be True or False
        valid_target_dir = os.path.commonpath([abs_working_dir, target_dir]) == abs_working_dir

        if valid_target_dir==False:
            return (f'Error: Cannot read "{file_path}" as it is outside the permitted working directory')
        if os.path.isfile(target_dir)==False:
            return f'Error: File not found or is not a regular file: "{file_path}"'
        with open(target_dir ,"r") as f:
            content=f.read(MAX_CHARS)
        # After reading the first MAX_CHARS...
            if f.read(1):
                content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
        return content
    except Exception as e:
        return f"Error: {e}"

schema_get_file_content = {
    "type": "function",
        "function": {
            "name": "get_file_content",
            "description": "get the content of a file ",
            "parameters": {
                "type": "object",
                "properties": {
                    "file_path": {
                     "type": "string",
                         "description": " file path to readfrom, relative to the working directory (default is the working directory itself)",
                    },
                },
                "required":["file_path"],
            },
        },
    }
