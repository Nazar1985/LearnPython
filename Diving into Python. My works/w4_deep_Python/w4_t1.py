import tempfile
import uuid
import os


class File:
    """Обработка текстовых файлов"""
    _curr = 0

    def __init__(self, path_to_file):
        """создание файла, либо обращение к существующему файлу"""
        self.path = path_to_file
        if not os.path.exists(self.path):
            with open(self.path, 'w', encoding='UTF-8') as f:
                f.write('')

    def __str__(self):
        """возвращает полный путь к фалу"""
        return self.path

    def __iter__(self):
        """позволяет произвести итерацию по строкам файла"""
        return self

    def __next__(self):
        """вызов следующей итерации"""
        with open(self.path, 'r', encoding="UTF-8") as file:
            lines = file.readlines()
        if self._curr < len(lines):
            line = lines[self._curr]
            self._curr += 1
            return line
        else:
            self._curr = 0
            raise StopIteration

    def __add__(self, other):
        """возвращает файл, содержащий строки из двух файлов"""
        new_path = os.path.join(tempfile.gettempdir(), str('cc' + uuid.uuid4().hex))
        with open(self.path, 'r', encoding="UTF-8") as first_file, \
                open(other.__str__(), 'r', encoding="UTF-8") as second_file:
            first_file = first_file.read()
            second_file = second_file.read()
            add_text = first_file + second_file
            new_file = File(new_path)
            new_file.write(add_text)
            return new_file

    def read(self):
        """чтение из файла"""
        if os.path.exists(self.path):
            with open(self.path, 'r', encoding='UTF-8') as file:
                return file.read()

    def write(self, text):
        """запись текста в файл"""
        with open(self.path, 'w', encoding="UTF-8") as file:
            return file.write(text)
