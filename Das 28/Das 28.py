import string
from string import digits


# 1․ Գրել BankUser class, որը․
#    - __init__() -ում կընդունի մարդու անունը, ազգանունը, տարիքը, հաշվեհամարը, գումարը հաշվեհամարի վրա, գաղտնաբառը,
#    - մինչ ինիցիալիզացնելը, կստուգի, որ ընդունված արգումենտները ճիշտ են մուտքագրված՝
#      -- անունը և ազգանունը - տառերից բաղկացած,+
#      -- տարիքը - ամբողջ թիվ,+
#      -- հաշվեհամարը - 16 թվանշանից բաղկացած (xxxx xxxx xxxx xxxx կամ xxxxxxxxxxxxxxxx ֆորմատով),+
#      -- գումարը - դրական թիվ,
#      -- գաղտնաբառը - ամենաքիչը 8 սիմվոլից բաղկացած տեքստ,
#    - անունը, ազգանունը և տարիքը կլինեն այնպիսի ատրիբուտներ, որոնց ուղիղ հասանելիությունը կլինի պաշտպանված,
#    - հաշվեհամարը, գումարը և գաղտնաբառը կլինեն այնպիսի ատրիբուտներ, որոնց ուղիղ հասանելիությունը կլինի արգելված,
#    - կունենա մեթոդ, որը կվերադարձնի մարդու անունը և ազգանունը,
#    - կունենա մեթոդ, որը կվերադարձնի մարդու տարիքը,
#    - կունենա մեթոդ, որը կվերադարձնի հաշվեհամարը և գումարը, բայց միայն ճիշտ գաղտնաբառ հավաքելուց հետո,
#    - կունենա մեթոդ, որը կավելացնի գումար հաշվին,
#    - կունենա մեթոդ, որը կհանի գումար հաշվից, հաշվի առեք, որ գումարը բացասական չի կարող լինել։

class Bank:

    def __init__(self, name, surname, age, _balance, _cash):
        if self.is_str(name, surname) and self.is_num(age) and self.is_balance(_balance) and self.is_cash(_cash) and \
                self.is_pass():

            self.name = name
            self.surname = surname
            self.age = age
            self._balance = _balance
            self._cash = _cash
        else:
            raise ValueError("Invalid name or surname format")

    @staticmethod
    def is_str(name, surname):
        if str(name)[0].isupper() and str(surname)[0].isupper():
            return True

    @staticmethod
    def is_num(age):
        if age % 1 == 0:
            return True

    def __str__(self):
        return f'Name: {self.name} \nSurname: {self.surname} \nAge: {self.age}, \nBalance: {self._balance}' \
               f'\nCash: {self._cash}'

    @staticmethod
    def is_balance(balance):
        if len(str(balance)) == 16 or len(str(balance)) == 19:
            return True

    @staticmethod
    def is_cash(cash):
        if cash >= 0:
            return True
        else:
            raise ValueError("Balance can't be < 0")

    @staticmethod
    def is_pass():
        password = 'qwerty1234'
        psw = input("Insert password: ")
        if psw == password and len(password) > 8:
            return True
        else:
            raise ValueError("Wrong or too short password")


a = Bank('Vahe', 'Badalyan', 28, '1234 1234 1234 1234', 100)
print(a)
