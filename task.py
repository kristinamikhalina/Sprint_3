import datetime

class OnlineSalesRegisterCollector:

    def __init__(self):
        self.__name_items = []
        self.__number_items = 0
        self.__item_price = {'чипсы': 50, 'кола': 100, 'печенье': 45, 'молоко': 55, 'кефир': 70}
        self.__tax_rate = {'чипсы': 20, 'кола': 20, 'печенье': 20, 'молоко': 10, 'кефир': 10}


    @property
    def name_items(self):
        return self.__name_items

    @property
    def number_items(self):
        return self.__number_items

    def add_item_to_cheque(self, name):
        try:
            if len(name) == 0 or len(name) > 40:
                raise ValueError('Нельзя добавить товар, если в его названии нет символов или их больше 40')

            if name not in self.__item_price:
                raise NameError('Позиция отсутствует в товарном справочнике')

            self.__name_items.append(name)
            self.__number_items += 1

        except ValueError as e:
            print(e)

        except NameError as e:
            print(e)

    def delete_item_from_check(self, name):
        try:
            if name not in self.__name_items:
                raise NameError('Позиция отсутствует в чеке')

            self.__number_items -= 1
            self.__name_items.remove(name)

        except NameError as e:
            print(e)

    def check_amount(self):
        total = 0
        for i in self.__name_items:
            price = self.__item_price[i]
            total += price

        if len(self.__name_items) > 10:
            total *= 0.9

        return total


    def twenty_percent_tax_calculation(self):
#тут хранятся имена товаров, у которых НДС 20%
        twenty_percent_tax = []
#тут хранятся цены товаров, у которых НДС 20%
        total = []

#проходим по главному списку и добавляем в наш новый товары с 20% НДС
        for i in self.__name_items:
            if self.__tax_rate[i] == 20:
                twenty_percent_tax.append(i)

#проходим по списку с ценами, и добавляем цены товаров в список с ценами наши товары
        for i in twenty_percent_tax:
            total.append(self.__item_price[i])

#список с голыми ценами товаров и умножаем все их на 20проц ндс, и учитываем условие скидки
        amount = sum(total)
        if len(self.__name_items) > 10:
            amount *= 0.9

        result = amount * 0.2
        return result

    def ten_percent_tax_calculation(self):
#тут хранятся имена товаров, у которых НДС 20%
        twenty_percent_tax = []
#тут хранятся цены товаров, у которых НДС 20%
        total = []

#проходим по главному списку и добавляем в наш новый - товары с 20% НДС
        for i in self.__name_items:
            if self.__tax_rate[i] == 10:
                twenty_percent_tax.append(i)

#проходим по списку с ценами, и добавляем цены товаров в список с ценами наши товары
        for i in twenty_percent_tax:
            total.append(self.__item_price[i])

#список с голыми ценами товаров и умножаем все их на 20проц ндс, и учитываем условие скидки
        amount = sum(total)
        if len(self.__name_items) > 10:
            amount *= 0.9

        result = amount * 0.1
        return result



    def total_tax(self):
        result = self.ten_percent_tax_calculation() + self.twenty_percent_tax_calculation()
        return result

    @staticmethod
    def get_telephone_number(telephone_number):
        try:
            if type(telephone_number) != int:
                raise ValueError('Необходимо ввести цифры')
            if len(str(telephone_number)) > 10:
                raise ValueError('Необходимо ввести 10 цифр после "+7"')

            return f'+7 {telephone_number}'
        except ValueError as e:
            print(e)






register_1 = OnlineSalesRegisterCollector()
register_1.add_item_to_cheque('чипсы')
register_1.add_item_to_cheque('чипсы')
register_1.add_item_to_cheque('чипсы')
register_1.add_item_to_cheque('чипсы')
register_1.add_item_to_cheque('чипсы')
register_1.add_item_to_cheque('чипсы')
register_1.add_item_to_cheque('чипсы')
register_1.add_item_to_cheque('чипсы')
register_1.add_item_to_cheque('чипсы')
register_1.add_item_to_cheque('чипсы')
register_1.add_item_to_cheque('молоко')
register_1.delete_item_from_check('молоко')
print(register_1.name_items)
print(register_1.check_amount())
print(register_1.twenty_percent_tax_calculation())
print(register_1.ten_percent_tax_calculation())
print(register_1.total_tax())
register_1.get_telephone_number('hi')