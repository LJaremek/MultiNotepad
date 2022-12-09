def get_file_name_from_path(path: str) -> str:
    homogeneous_path: str = path.replace("\\", "/")
    homogeneous_path: list[str] = homogeneous_path.split("/")
    file_with_format: str = homogeneous_path[-1]
    file_name: str = file_with_format.split(".")[0]
    return file_name
