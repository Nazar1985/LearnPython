import tempfile
import argparse
import json
import os


def get_param():
    """ Получение параметров из командной строки """
    parser = argparse.ArgumentParser()
    parser.add_argument('--key', help='use for choose key')
    parser.add_argument('--val', help='use for save value')
    args = parser.parse_args()
    return args.key, args.val


def write_in_file(data):
    """ Запись данных в файл """
    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
    with open(storage_path, 'w') as f:
        json.dump(data, f)


def read_from_file():
    """ Чтение данных из файла """
    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
    with open(storage_path, 'r') as f:
        data = json.load(f)
        return data


def main():
    """ Основная логика приложения приложения """
    # получение ключа и его значения из командной строки
    key, val = get_param()
    try:
        # Открыть и прочитать файл для обработки словаря
        data_file = read_from_file()
        if key and val:
            if key in data_file.keys():
                data = dict()
                data[key] = data_file.get(key) + ', ' + val
                data_file.update(data)
                write_in_file(data_file)
            else:
                data_file[key] = val
                write_in_file(data_file)
        elif key and not val:
            # Вывод знаения для ключа
            # если в командной строке не передано значение
            print(data_file.get(key))
        else:
            return None
    except FileNotFoundError:
        if key and val:
            data_file = dict()
            data_file[key] = val
            write_in_file(data_file)
        else:
            return None
    except json.decoder.JSONDecodeError:
        if key and val:
            data_file = dict()
            data_file[key] = val
            write_in_file(data_file)
        else:
            return None


if __name__ == '__main__':
    main()
