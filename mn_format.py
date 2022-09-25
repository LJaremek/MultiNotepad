"""
>> mn format file documentation <<

mn format is a normal zip archive with changed name.

You can simply open mn file with Python zipfile library
or 7zip program (open source free software).

mn file contains flat files (as txt, json, py),
which are notepads in  MultiNotepad.
"""

import zipfile


def open_mn_file(
        path: str,
        encoding: str = "utf-8"
        ) -> dict[str]:
    """
    Opening mn file.
    Input:
     * path: str - path with file name and file format
     * encoding: str - encoding of flat files in mn file. Default: utf-8

    Output:
    * files data: dict[str, str] - dict with files data, key is file name,
                                   value is file content.

    Example:
        my_data = open_mn_file("Documents/work.mn")

        to_do_content = my_data["to_do.txt"]
    """
    results: dict[str, str] = {}

    with zipfile.ZipFile(path, "r") as archive:
        for file_zip_name in archive.filelist:
            file_data = archive.read(file_zip_name).decode(encoding)

            results[file_zip_name] = file_data

    return results


def save_mn_file(
        path: str,
        files_data: dict[str, str],
        encoding: str = "utf-8"
        ) -> None:
    """
    Saving mn file.
    Input:
     * path: str - path with file name and file format
     * files_data: dict[str, str] - content of flat files.
        Key is file name, value is file content.
     * encoding: str - encoding of flat files in mn file. Default: utf-8

    Example:
        my_data = save_mn_file("Documents/work.mn", {"to_do.txt": "buy milk"})
    """
    with zipfile.ZipFile(path, "w") as archive:
        for file_name in files_data:
            with archive.open(file_name, "w") as zip_file:
                zip_file.write(bytes(files_data[file_name], encoding=encoding))


if __name__ == "__main__":
    files_data = open_mn_file("mn_samples/sample.mn")

    files_data["new_file.py"] = "print('I love Python!')\n"

    save_mn_file("mn_samples/new_sample.mn", files_data)
