# /usr/bin/python
# -*- coding: utf-8 -*-

class Customers:
    def __init__(self,first_name,second_name,city,balance):
        self.first_name = first_name
        self.second_name = second_name
        self.city = city
        self.balance = balance
    def str(self):
        return f'"{self.first_name} {self.second_name}. {self.city}. Баланс: {self.balance} руб."'

customers_1 = Customers('Иван','Петров','Москва',50)
print(customers_1.str())