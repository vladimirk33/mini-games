# Счёт, пожалуйста!
# несложное ресторанное меню с блюдами и ценами
# принятие заказа и вывод на экран суммы счёта
import tkinter as tk
from tkinter.constants import *
from collections import OrderedDict

class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.total = 0
        self.grid()
        self.create_widgets()
    def create_widgets(self): 
        # метка с текстом-инструкцией
        tk.Label(self,
                 text='Выберите блюда, которые вы хотите заказать: ',
                 ).grid(row=0, column=0, columnspan=3, sticky=W)
        # словарь с блюдами
        self.dishes = OrderedDict({'итальянская лазанья' : 1500,
                                   'русский борщ' : 1000,
                                   'грибное рагу' : 1200,
                                   'сельдь под шубой' : 800,
                                   'салат "Оливье"' : 600,
                                  })
        # заголовки таблицы
        tk.Label(self,
                 text='Блюдо'
                 ).grid(row=1, column=0, sticky=W)
        tk.Label(self,
                 text='Цена'
                 ).grid(row=1, column=1, sticky=W)
        row = 2
        # вывод блюд из цен из словаря
        self.checkbutton_list = []
        for dish_name, dish_price in self.dishes.items():
            tk.Label(self,
                     text='- ' + dish_name
                     ).grid(row=row, column=0, sticky=W)
            tk.Label(self,
                     text=str(dish_price) + ' руб.'
                     ).grid(row=row, column=1, sticky=W)
            is_clicked = tk.BooleanVar()
            self.checkbutton_list.append(is_clicked)
            tk.Checkbutton(self,
                           variable=is_clicked,
                           ).grid(row=row, column=2, sticky=W)
            row += 1
        # кнопка сабмита
        tk.Button(self,
                  text='Сделать заказ',
                  command=self.total_sum
                  ).grid(row=len(self.dishes) + 2, column=0, sticky=W)
        # начальная метка с суммой
        self.price_label = tk.Label(self,
                                    text='Сумма заказа: ' + str(self.total)
                                    + ' руб.')
        self.price_label.grid(row=len(self.dishes) + 2, column=1, sticky=W)
        
    def total_sum(self):
        '''Вывод общей суммы на экран.'''
        self.total = 0
        i = 0
        for dish_price in self.dishes.values():
            if self.checkbutton_list[i].get():
                self.total += dish_price
            i += 1
        self.price_label.destroy()
        self.price_label = tk.Label(self,
                                    text='Сумма заказа: ' + str(self.total)
                                    + ' руб.')
        self.price_label.grid(row=len(self.dishes) + 2, column=1, sticky=W)
        self.print_receipt()

    def print_receipt(self):
        '''Печатает чек в поле текста.'''
        self.receipt_txt = tk.Text(self, width=75, height=10, wrap=WORD)
        if not self.total:
            self.receipt_txt.grid(row=len(self.dishes) + 3, column=0, \
                                  columnspan=4)
            self.receipt_txt.delete(0.0, END)
        else:
            self.receipt_txt.grid(row=len(self.dishes) + 3, column=0, \
                                  columnspan=4)
            self.receipt_txt.delete(0.0, END)
            receipt = '\tВаш чек:\n\n'
            i = 0
            cnt = 1
            for dish_name, dish_price in self.dishes.items():
                if not self.checkbutton_list[i].get():
                    i += 1
                    continue                   
                receipt += str(cnt) + '. ' + dish_name.capitalize() + '\n'
                receipt += 'Цена: ' + str(dish_price) + '\n'
                receipt += '-' * 25 + '\n'
                i += 1
                cnt += 1
            receipt += '\nОбщая цена: ' + str(self.total)
            self.receipt_txt.insert(0.0, receipt)

root = tk.Tk()
root.title('Ресторанное меню')
app = Application(root)
root.mainloop()
