'''Функции с несколькими обработчиками разных типов исключений'''
from Exceptions import InvalidOrderError
from Exceptions import UserNotFoundError


def book_order(order_amount):
    """ Обработка заказа с несколькими обработчиками исключений """
    try:
        if order_amount < 0:
            raise ValueError("Количество товаров в заказе не может быть меньше 0")
        elif order_amount == 0:
            raise InvalidOrderError("Ничего не добавлено в заказ")
        print(f"Заказ с количеством книг {order_amount} принят")
    except ValueError as ve:
        print(ve)
    except InvalidOrderError as te:
        print(te)
    finally:
        print("Обработка заказа завершена\n")

def find_user(users, user_id):
    "Поиск пользователя с обработкой нескольких исключений"
    try:
        if user_id not in users:
            raise UserNotFoundError(f"Пользователь с ID {user_id} не найден")
        user = users[user_id]
        print(f"найден пользователь: {user}")
        return user
    except UserNotFoundError as ue:
        print(ue)
    except KeyError as ke:
        print(f"Ошибка ключаЖ {ke}")
    finally:
        print("Завершение поиска пользователя\n")

def discount_price(price, discount):
    """Рассчет скидки с несколькими обработчиками исключений"""
    try:
        if price < 0:
            raise ValueError("Цена не может быть отрицательной")
        if discount < 0 or discount > 100:
            raise ValueError("Скидка должна быть в пределах 0-100")
        discounted_price = price - (price * discount / 100)
        print(f"Цена после скидки: {discounted_price}")
        return discounted_price
    except ValueError as ve:
        print(f"Ошибка данных: {ve}")
    except TypeError as te:
        print(f"Неправильный тип данных {te}")
    except Exception as e:
        print(f"Ошибка: {e}")