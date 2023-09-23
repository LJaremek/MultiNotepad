from .mn_format import open_mn_file, save_mn_file


class Notepad:
    def __init__(
            self,
            name: str,
            content: str,
            index: int,
            format: str
            ) -> None:

        self.name = name
        self.content = content
        self.index = index
        self.format = format

    def __str__(self) -> str:
        return f"Notepad Class. I:{self.index} N:{self.name} C:{self.content}"

    def __repr__(self) -> str:
        return self.__str__()


class MultiNotepadManager:
    def __init__(self) -> None:
        self._content: list[Notepad] = []

    def _update_notepads_index(self) -> None:
        for index in range(len(self._content)):
            self._content[index].index = index

    def size(self) -> int:
        return len(self._content)

    def clear(self) -> None:
        print("[!] CLEARING")
        self._content = []

    def add_notepad(
            self,
            name: str,
            content: str,
            index: int = None,
            format: str = "txt"
            ) -> None:

        if index is None:
            index = len(self._content)

        self._content.insert(index, Notepad(name, content, None, format))
        self._update_notepads_index()

    def remove_notepad(self, name: str = None, index: int = None) -> bool:
        if index is None and name is None:
            raise Exception("You have to specify Notepad index or name!")

        index_to_delete: int = None

        loop_broken = False
        if name is not None:
            for i, notepad in enumerate(self._content):
                if notepad.name == name:
                    if index is not None and index != i:
                        raise Exception("Notepad name and index does not fit!")
                    index_to_delete = i
                    loop_broken = True
                    break
            if not loop_broken:
                raise Exception(f"Notepad with name '{name}' does not exists!")
        else:
            if name is not None and self.get_notepad(name=name).index != index:
                raise Exception("Notepad index and name does not fit!")
            index_to_delete = index

        if index_to_delete is None:
            return False

        del self._content[index_to_delete]
        self._update_notepads_index()
        return True

    def get_notepad(self, index: int = None, name: str = None) -> Notepad:
        if index is None and name is None:
            raise Exception("You have to specify Notepad index or name!")

        if index is not None:
            notepad = self._content[index]
            if name is not None and notepad.name != name:
                raise Exception("Notepad index and name does not fit!")
            return notepad

        for i, notepad in enumerate(self._content):
            if notepad.name == name:
                if index is not None and i != index:
                    raise Exception("Notepad name and index does not fit!")
                return notepad

    def update_notepad_name(
            self,
            new_name: str,
            index: int = None,
            name: str = None
            ) -> None:

        if index is None and name is None:
            raise Exception("You have to specify Notepad index or name!")

        if index is not None:
            if name is not None and self._content[index].name != name:
                raise Exception("Notepad index and name does not fit!")
            self._content[index].name = new_name

        for i, notepad in enumerate(self._content):
            if notepad.name == name:
                if index is not None and i != index:
                    raise Exception("Notepad name and index does not fit!")
                self._content[i].name = new_name

    def update_notepad_content(
            self,
            new_content: str,
            index: int = None,
            name: str = None
            ) -> None:

        if index is None and name is None:
            raise Exception("You have to specify Notepad index or name!")

        if index is not None:
            if name is not None and self._content[index].name != name:
                raise Exception("Notepad index and name does not fit!")
            self._content[index].content = new_content

        for i, notepad in enumerate(self._content):
            if notepad.name == name:
                if index is not None and i != index:
                    raise Exception("Notepad name and index does not fit!")
                self._content[i].content = new_content

    def update_notepad_index(
            self,
            new_index: int,
            index: int = None,
            name: str = None
            ) -> None:

        if index is None and name is None:
            raise Exception("You have to specify Notepad index or name!")

        if index is None:
            loop_broken = False
            for i in range(len(self._content)):
                if self._content[i].name == name:
                    loop_broken = True
                    index = i
                    break
            if not loop_broken:
                raise Exception(f"Notepad with name '{name}' does not exists!")

        if new_index == index:
            return

        notepad = self._content.pop(index)
        self.add_notepad(
            notepad.name, notepad.content, new_index, notepad.format
            )

    def load_mn_file(self, path: str) -> None:
        self.clear()
        mn_data = open_mn_file(path)

        for file_name in mn_data:
            file = mn_data[file_name]

            self._content.append(
                Notepad(
                    name=file.file_name,
                    content=file.file_content,
                    index=-1,
                    format=file.file_format
                    )
                )

    def save_mn_file(self, path) -> None:
        data = {}

        for notepad in self._content:
            data[notepad.name+"."+notepad.format] = notepad.content

        save_mn_file(path, data)
