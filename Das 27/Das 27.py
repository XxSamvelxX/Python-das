# 1․ Գրել Triangle class, որը․
#    - __init__() -ում կընդունի եռանկյան կողմերը և կստուգի արդյոք նման կողմերով եռանկյուն գոյություն ունի թե ոչ,
#      եթե կողմերը սխալ են տրված կվերադարձնի Error համապատասխան տեքստով,
#    - կունենա մեթոդ, որը կվերադարձնի եռանկյան կողմերը,
#    - կունենա մեթոդ, որը կվերադարձնի եռանկյան պարագիծը,
#    - կունենա մեթոդ, որը կվերադարձնի եռանկյան մակերեսը,
#    - կունենա մեթոդ, որը կվերադարձնի արդյոք եռանկյունը հավասարակողմ է, հավասարասրուն, թե անկանոն (կողմերը իրար = չեն)։

class Triangle:
    """Ծրագիրը վերադարձնում է տրված կողմերը, նաև հաշվում եռանկյան պարագիծը, մակերեսը,նրա տեսակը և արդյո՞ք  գոյություն ունի տրված կողմերով եռանկյուն"""

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        if self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a:

    def __str__(self):
        return f"{self.a} {self.b} {self.c}"

    def par(self):
        return self.a + self.b + self.c

    def makeres(self):
        kes = (self.a + self.b + self.c) / 2
        
            return round((kes * (kes - self.a) * (kes - self.b) * (kes - self.c)) ** 0.5, 2)
        else:
            raise Exception("Invalid parameters")

    def tesak(self):
        if self.a == self.b == self.c:
            return "Havasarakoxm erankyun"
        if self.a == self.b or self.b == self.c or self.a == self.c:
            return "Havasarasrun erankyun"
        if self.a != self.b or self.b != self.c or self.a != self.c:
            return "Ankanon erankyun"


# ---------------------------------------------------- Class workspace --------------------------------------------


triangle = Triangle(10, 41, 8)
print(triangle.__doc__)
print(triangle)
print(triangle.par(), '-paragic')
print(triangle.makeres())
print(triangle.tesak())

