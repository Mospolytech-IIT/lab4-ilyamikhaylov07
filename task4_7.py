'''Функция с применением пользовательского исключения'''
from Exceptions import PaymentError
def payment_book(amount, price):
    "Функция оплаты заказа книг"
    try:
        if amount < 0:
            raise PaymentError("Количество книг не может быть меньше 0")
        if price < 0:
            raise PaymentError("Цена не может быть меньше 0")
        print("Спасибо за покупку!")
    except PaymentError as pe:
        print(f"Ошибка: {pe}")
