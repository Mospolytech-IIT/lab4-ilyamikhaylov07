''' Классы пользовательских исключений, наследованных от базового Exception'''

class InvalidOrderError(Exception):
    print("Пользовательское исключение для некорректного заказа")

class UserNotFoundError(Exception):
    print("Пользовательское исключение для отсутствующего пользователя")

class PaymentError(Exception):
    print("Пользовательское исключение для ошибок при оплате")