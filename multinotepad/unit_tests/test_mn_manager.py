from ..mn_manager import MultiNotepadManager


def test_empty_manager() -> None:
    mn_manager = MultiNotepadManager()
    assert mn_manager.size() == 0
    assert mn_manager._content == []


def test_add_notepad_1() -> None:
    mn_manager = MultiNotepadManager()
    mn_manager.add_notepad("first", "Pan Tadeusz")
    assert mn_manager.size() == 1
    assert mn_manager.get_notepad(0).content == "Pan Tadeusz"
    assert mn_manager.get_notepad(0).index == 0
    assert mn_manager.get_notepad(0).name == "first"


def test_add_notepad_2() -> None:
    mn_manager = MultiNotepadManager()
    mn_manager.add_notepad("first", "Pan Tadeusz")
    mn_manager.add_notepad("second", "Lalka")
    assert mn_manager.size() == 2
    assert mn_manager.get_notepad(0).content == "Pan Tadeusz"
    assert mn_manager.get_notepad(0).index == 0
    assert mn_manager.get_notepad(0).name == "first"
    assert mn_manager.get_notepad(1).content == "Lalka"
    assert mn_manager.get_notepad(1).index == 1
    assert mn_manager.get_notepad(1).name == "second"


def test_add_notepad_3() -> None:
    mn_manager = MultiNotepadManager()
    mn_manager.add_notepad("first", "Pan Tadeusz")
    mn_manager.add_notepad("second", "Lalka", 0)
    assert mn_manager.size() == 2
    assert mn_manager.get_notepad(1).content == "Pan Tadeusz"
    assert mn_manager.get_notepad(1).index == 1
    assert mn_manager.get_notepad(1).name == "first"
    assert mn_manager.get_notepad(0).content == "Lalka"
    assert mn_manager.get_notepad(0).index == 0
    assert mn_manager.get_notepad(0).name == "second"


def test_add_notepad_4() -> None:
    mn_manager = MultiNotepadManager()
    mn_manager.add_notepad("first", "Pan Tadeusz")
    mn_manager.add_notepad("second", "Lalka", 0)
    mn_manager.add_notepad("third", "Dziady")
    assert mn_manager.size() == 3
    assert mn_manager.get_notepad(1).content == "Pan Tadeusz"
    assert mn_manager.get_notepad(1).index == 1
    assert mn_manager.get_notepad(1).name == "first"
    assert mn_manager.get_notepad(0).content == "Lalka"
    assert mn_manager.get_notepad(0).index == 0
    assert mn_manager.get_notepad(0).name == "second"
    assert mn_manager.get_notepad(2).content == "Dziady"
    assert mn_manager.get_notepad(2).index == 2
    assert mn_manager.get_notepad(2).name == "third"


def test_remove_notepad_1a() -> None:
    mn_manager = MultiNotepadManager()
    mn_manager.add_notepad("first", "Pan Tadeusz")
    mn_manager.remove_notepad(name="first")
    assert mn_manager.size() == 0
    assert mn_manager._content == []


def test_remove_notepad_1b() -> None:
    mn_manager = MultiNotepadManager()
    mn_manager.add_notepad("first", "Pan Tadeusz")
    mn_manager.remove_notepad(index=0)
    assert mn_manager.size() == 0
    assert mn_manager._content == []


def test_remove_notepad_2a() -> None:
    mn_manager = MultiNotepadManager()
    mn_manager.add_notepad("first", "Pan Tadeusz")
    try:
        mn_manager.remove_notepad(name="first", index=1)
        assert False
    except Exception as e:
        assert e.__str__() == "Notepad name and index does not fit!"


def test_remove_notepad_2b() -> None:
    mn_manager = MultiNotepadManager()
    mn_manager.add_notepad("first", "Pan Tadeusz")
    try:
        mn_manager.remove_notepad(name="second", index=0)
        assert False
    except Exception as e:
        assert e.__str__() == "Notepad with name 'second' does not exists!"


def test_remove_notepad_3() -> None:
    mn_manager = MultiNotepadManager()
    mn_manager.add_notepad("first", "Pan Tadeusz")
    mn_manager.add_notepad("second", "Lalka")
    mn_manager.remove_notepad("second")
    assert mn_manager.size() == 1
    assert mn_manager.get_notepad(0).content == "Pan Tadeusz"
    assert mn_manager.get_notepad(0).index == 0
    assert mn_manager.get_notepad(0).name == "first"


def test_remove_notepad_4() -> None:
    mn_manager = MultiNotepadManager()
    mn_manager.add_notepad("first", "Pan Tadeusz")
    mn_manager.add_notepad("second", "Lalka")
    mn_manager.remove_notepad("first")
    assert mn_manager.size() == 1
    assert mn_manager.get_notepad(0).content == "Lalka"
    assert mn_manager.get_notepad(0).index == 0
    assert mn_manager.get_notepad(0).name == "second"


def test_remove_notepad_5() -> None:
    mn_manager = MultiNotepadManager()
    mn_manager.add_notepad("first", "Pan Tadeusz")
    mn_manager.add_notepad("second", "Lalka")
    mn_manager.add_notepad("third", "Dziady")
    mn_manager.remove_notepad(index=2)
    mn_manager.remove_notepad(name="first")
    mn_manager.remove_notepad(index=0)
    assert mn_manager.size() == 0
    assert mn_manager._content == []


def test_update_name_1() -> None:
    mn_manager = MultiNotepadManager()
    mn_manager.add_notepad("first", "Pan Tadeusz")
    mn_manager.update_notepad_name("Tadek", name="first")
    assert mn_manager.get_notepad(0).name == "Tadek"
    assert mn_manager.get_notepad(0).index == 0
    assert mn_manager.get_notepad(0).content == "Pan Tadeusz"


def test_update_name_2() -> None:
    mn_manager = MultiNotepadManager()
    mn_manager.add_notepad("first", "Pan Tadeusz")
    mn_manager.add_notepad("second", "Lalka")
    mn_manager.update_notepad_name("TEST", index=0)
    assert mn_manager.get_notepad(0).name == "TEST"
    assert mn_manager.get_notepad(0).index == 0
    assert mn_manager.get_notepad(0).content == "Pan Tadeusz"
    assert mn_manager.get_notepad(1).name == "second"
    assert mn_manager.get_notepad(1).index == 1
    assert mn_manager.get_notepad(1).content == "Lalka"


def test_update_name_3() -> None:
    mn_manager = MultiNotepadManager()
    mn_manager.add_notepad("first", "Pan Tadeusz")
    mn_manager.add_notepad("second", "Lalka")
    try:
        mn_manager.update_notepad_name("Dziady")
        assert False
    except Exception as e:
        assert e.__str__() == "You have to specify Notepad index or name!"


def test_update_content_1() -> None:
    mn_manager = MultiNotepadManager()
    mn_manager.add_notepad("first", "Pan Tadeusz")
    mn_manager.update_notepad_content("Lalka jednak", index=0)
    assert mn_manager.get_notepad(0).name == "first"
    assert mn_manager.get_notepad(0).index == 0
    assert mn_manager.get_notepad(0).content == "Lalka jednak"


def test_update_content_2() -> None:
    mn_manager = MultiNotepadManager()
    mn_manager.add_notepad("first", "Pan Tadeusz")
    mn_manager.add_notepad("second", "Lalka")
    mn_manager.update_notepad_content("Dziady", index=1)
    assert mn_manager.get_notepad(1).name == "second"
    assert mn_manager.get_notepad(1).index == 1
    assert mn_manager.get_notepad(1).content == "Dziady"


def test_update_content_3() -> None:
    mn_manager = MultiNotepadManager()
    mn_manager.add_notepad("first", "Pan Tadeusz")
    mn_manager.add_notepad("second", "Lalka")
    try:
        mn_manager.update_notepad_content("Dziady", index=1, name="Tadek")
        assert False
    except Exception as e:
        assert e.__str__() == "Notepad index and name does not fit!"


def test_update_index_1() -> None:
    mn_manager = MultiNotepadManager()
    mn_manager.add_notepad("first", "Pan Tadeusz")
    mn_manager.update_notepad_index(1, 0)
    assert mn_manager.get_notepad(0).name == "first"
    assert mn_manager.get_notepad(0).index == 0
    assert mn_manager.get_notepad(0).content == "Pan Tadeusz"


def test_update_index_2() -> None:
    mn_manager = MultiNotepadManager()
    mn_manager.add_notepad("first", "Pan Tadeusz")
    mn_manager.add_notepad("second", "Lalka")
    mn_manager.update_notepad_index(1, 0)
    assert mn_manager.get_notepad(1).name == "first"
    assert mn_manager.get_notepad(1).index == 1
    assert mn_manager.get_notepad(1).content == "Pan Tadeusz"
    assert mn_manager.get_notepad(0).name == "second"
    assert mn_manager.get_notepad(0).index == 0
    assert mn_manager.get_notepad(0).content == "Lalka"


def test_update_index_3() -> None:
    mn_manager = MultiNotepadManager()
    mn_manager.add_notepad("first", "Pan Tadeusz")
    mn_manager.add_notepad("second", "Lalka")
    mn_manager.add_notepad("third", "Dziady")
    mn_manager.update_notepad_index(1, name="third")
    assert mn_manager.get_notepad(0).name == "first"
    assert mn_manager.get_notepad(0).index == 0
    assert mn_manager.get_notepad(0).content == "Pan Tadeusz"
    assert mn_manager.get_notepad(1).name == "third"
    assert mn_manager.get_notepad(1).index == 1
    assert mn_manager.get_notepad(1).content == "Dziady"
    assert mn_manager.get_notepad(2).name == "second"
    assert mn_manager.get_notepad(2).index == 2
    assert mn_manager.get_notepad(2).content == "Lalka"


def test_update_index_4() -> None:
    mn_manager = MultiNotepadManager()
    mn_manager.add_notepad("first", "Pan Tadeusz")
    mn_manager.add_notepad("second", "Lalka")
    mn_manager.add_notepad("third", "Dziady")
    try:
        mn_manager.update_notepad_index(1, name="Dziady")
        assert False
    except Exception as e:
        assert e.__str__() == "Notepad with name 'Dziady' does not exists!"
