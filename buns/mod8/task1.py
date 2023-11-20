class Transport:
    def __init__(self, *args, **kwargs):
        self.__coordinates, self.__speed, self.__brand, self.__year, self.__number = args[:5]

    @property
    def coordinates(self):
        return self.coordinates

    @coordinates.setter
    def coordinates(self, coordinates):
        self.__coordinates = coordinates

    @property
    def speed(self):
        return self.speed

    @speed.setter
    def speed(self, speed):
        self.__speed = speed

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, brand):
        self.__brand = brand

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        self.__year = year

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number):
        self.__number = number

    def __str__(self):
        return f"({self.coordinates}) {self.speed}км/ч {self.brand}({self.year})№{self.number}"

    def is_in_area(self, pos_x, pos_y, length, width) -> bool:
        x, y = self.coordinates
        return pos_x <= x <= pos_x + width and pos_y <= y <= pos_y + length


class Passenger(Transport):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__passengers_capacity = args[5]
        self.__number_of_passengers = args[6]

    @property
    def passengers_capacity(self):
        return self.__passengers_capacity

    @passengers_capacity.setter
    def passengers_capacity(self, passengers_capacity):
        self.__passengers_capacity = passengers_capacity

    @property
    def number_of_passengers(self):
        return self.__number_of_passengers

    @number_of_passengers.setter
    def number_of_passengers(self, number_of_passengers):
        self.__number_of_passengers = number_of_passengers


class Cargo(Transport):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__carrying = args[5]

    @property
    def carrying(self):
        return self.__carrying

    @carrying.setter
    def carrying(self, carrying):
        self.__carrying = carrying


class Plane(Transport):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__height = args[5]

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height


class Auto(Transport):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Ship(Transport):
    def __init__(self, *args, **kwargs):
        super().__init__(args[2:], **kwargs)
        self.__name = args[0]
        self.__port = args[1]

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def port(self):
        return self.__port

    @port.setter
    def port(self, port):
        self.__port = port


class Car(Auto):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Bus(Auto, Passenger):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class CargoAuto(Auto, Cargo):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Boat(Ship):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class PassengerShip(Ship, Passenger):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class CargoShip(Ship, Cargo):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Airplane(Ship):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class PassengerPlane(Ship, Passenger):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class CargoPlane(Ship, Cargo):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class SeaPlane(Plane, Ship):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)