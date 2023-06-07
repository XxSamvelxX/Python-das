from abc import ABC, abstractmethod
import math

# 1․ Գրել Shape abstract class, որը․
#    - կունենա __init__(), perimetr(), area() աբստրակտ մեթոդներ։
# 2․ Գրել Circle class, որը կժառանգի Shape class-ից, որը․
#    - __init__() -ում կընդունի շրջանագծի շառավիղը,
#    - մինչ ինիցիալիզացնելը, կստուգի, որ ընդունված արգումենտը ճիշտ մուտքագրված լինի (պետք է լինի դրական թիվ),
#    - կվերախմբագրի Shape class-ի perimetr() և area() մեթոդները շրջանագծի համար։
# 3․ Գրել Rectangle class, որը կժառանգի Shape class-ից, որը․
#    - __init__() -ում կընդունի ուղղանկյան լայնությունը և երկարությունը,
#    - մինչ ինիցիալիզացնելը, կստուգի, որ ընդունված արգումենտները ճիշտ մուտքագրված լինեն (պետք է լինեն դրական թվեր),
#    - կվերախմբագրի Shape class-ի perimetr() և area() մեթոդները ուղղանկյան համար։
# 4․ Գրել Triangle class, որը կժառանգի Shape class-ից, որը․
#    - __init__() -ում կընդունի
#      -- կամ եռանկյան երեք կողմերը,
#      -- կամ մեկ կողմը և բարձրությունը,
#      -- կամ երկու կողմերը և այդ կողմերի կազմած անկյունը,
#    - մինչ ինիցիալիզացնելը, կստուգի, որ ընդունված արգումենտները ճիշտ մուտքագրված լինեն,
#    - կվերախմբագրի Shape class-ի perimetr() մեթոդը եռանկյան համար,
#    - եռանկյան մակերեսը կհաշվի 3 տարբերակով, կախված մուտքագրված պարամետրերից․
#      1) S = (p * (p - a) * (p - b) * (p - c)) ^ 0.5   , որտեղ a, b, c - եռանկյան կողմերն են, p - եռանկյան կիսապարագիծը,
#      2) S = a * h / 2                                 , որտեղ a - եռանկյան կողմը, h = եռանկյան բարձրությունը,
#      3) S = a * b * sin(alpha) / 2                    , որտեղ a, b - եռանկյան կողմերն են, alpha - եռանկյան a և b կողմերի կազմած անկյունը։

class Shape(ABC):

    @abstractmethod
    def area(self):
        print('Model: ')

    @abstractmethod
    def par(self):
        print('Year: ')


# c = Car()  # error


class Circle(Shape):

    def __init__(self, r):
        self.r = r

    def area(self):
        return round((self.r * 3.14) ** 2, 2)

    def par(self):
        return round(self.r * 2 * 3.14, 2)


# c = Circle(10)
# print(c.area())
# print(c.par())


class Square(Shape):

    def __init__(self, k):
        self.k = k

    def par(self):
        return 4 * self.k

    def area(self):
        return self.k ** 2


# s = Square(10)
# print(s.par())
# print(s.area())


class Rect(Shape):

    def __init__(self, rec, rec1):
        self.rec = rec
        self.rec1 = rec1

    def par(self):
        return 2 * self.rec + 2 * self.rec1

    def area(self):
        return self.rec * self.rec1


# rec = Rect(10, 15)
# print(rec.par())
# print(rec.area())


class Triangle(Shape):

    def __init__(self, a, b, c, himq, height, alfa):
        self.height = height
        self.alfa = alfa
        self.himq = himq
        self.a = a
        self.b = b
        self.c = c

    def par(self):
        return self.a + self.b + self.c

    def area(self):
        kes = (self.a + self.b + self.c) / 2
        return (kes * (kes - self.a) * (kes - self.b) * (kes - self.c)) ** 0.5

    def area_1(self):
        return self.himq * self.height / 2

    def area_2(self):
        return self.a * self.b * math.sin(math.radians(self.alfa))


# t = Triangle(10, 10, 10, 10, 13, 60)
# print(t.par())
# print(t.area())
# print(t.area_1())
# print(t.area_2())


