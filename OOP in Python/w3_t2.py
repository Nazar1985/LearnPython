import csv
import os
import string


def parser_str(x):
    return x.isalpha() and x or x.isdigit() and int(x) or x.isalnum() and x or \
           len(set(string.punctuation).intersection(x)) == 1 and x.count('.') == 1 and float(x) or x


class CarBase:

    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying)

    def get_photo_file_ext(self):
        """Получение расширения файла изображения"""
        ext = os.path.splitext(self.photo_file_name)[-1]
        return ext


class Car(CarBase):
    car_type = 'car'  # Тип машины - значение из списка

    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = int(passenger_seats_count)


class Truck(CarBase):
    car_type = 'truck'  # Тип машины - значение из списка

    def __init__(self, brand, photo_file_name, carrying, body_whl):
        body_lwh = body_whl.split('x')
        super().__init__(brand, photo_file_name, carrying)
        self.body_length = float(body_lwh[0]) if body_whl != '' and len(body_lwh) == 3 and (isinstance(parser_str(body_lwh[0]), float) or isinstance(parser_str(body_lwh[0]), int)) else 0.0
        self.body_width = float(body_lwh[1]) if body_whl != '' and len(body_lwh) == 3 and (isinstance(parser_str(body_lwh[1]), float) or isinstance(parser_str(body_lwh[1]), int)) else 0.0
        self.body_height = float(body_lwh[2]) if body_whl != '' and len(body_lwh) == 3 and (isinstance(parser_str(body_lwh[2]), float) or isinstance(parser_str(body_lwh[2]), int)) else 0.0

    def get_body_volume(self):
        return self.body_height * self.body_width * self.body_length


class SpecMachine(CarBase):
    car_type = 'spec_machine'  # Тип машины - значение из списка

    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = extra       # Дополнительное описание машины


def get_car_list(csv_file_name):
    ext_list = ['.jpg', '.jpeg', '.png', '.gif']
    car_list = []
    try:
        with open(csv_file_name, encoding="utf8") as csv_f:
            r = csv.reader(csv_f, delimiter=';')
            next(r)
            for row in r:
                len_row = len(row)
                if len_row == 7:
                    type_car, brand, pas, photo, body_whl, carr, extra = row
                    brand = brand if brand and not brand.isdigit() else False
                    ext_photo = os.path.splitext(photo)[-1]
                    photo = photo if photo and ext_photo in ext_list else False
                    pas = int(pas) if pas.isdigit() else False
                    carr = float(carr) if isinstance(parser_str(carr), float) or isinstance(parser_str(carr), int) \
                        else False
                    b_sp = body_whl.split('x')
                    body_whl = body_whl if body_whl == '' or (len(b_sp) == 3 and not b_sp[0].isalpha() and not b_sp[1].isalpha() and not b_sp[2].isalpha()) \
                        else False
                    extra = extra if extra else False
                    if brand and photo and carr:
                        if type_car == 'car' and pas:
                            car = Car(brand, photo, carr, pas)
                            car_list.append(car)
                        elif type_car == 'truck' and (body_whl or body_whl == ''):
                            truck = Truck(brand, photo, carr, body_whl)
                            car_list.append(truck)
                        elif type_car == 'spec_machine' and extra:
                            spec_machine = SpecMachine(brand, photo, carr, extra)
                            car_list.append(spec_machine)
    except IOError:
        pass
    return car_list
