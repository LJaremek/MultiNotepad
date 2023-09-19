from ..tools.text_tools import get_file_name_from_path


def test_path_1() -> None:
    path = "C:\\Users\\User1\\my_file.txt"
    assert "my_file" == get_file_name_from_path(path)


def test_path_2() -> None:
    path = "C:/Users/User1/my_file.txt"
    assert "my_file" == get_file_name_from_path(path)


def test_path_3() -> None:
    path = "C:\\Users/User1\\some_folder/my_file.txt"
    assert "my_file" == get_file_name_from_path(path)


def test_path_4() -> None:
    path = "C:\\Users\\User1\\very/long\\path/because\\why/not\\xd/my_file.txt"
    assert "my_file" == get_file_name_from_path(path)
