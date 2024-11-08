'''start point main'''

from task4_1 import check_name, check_age
from task4_2 import take_elbook
from task4_3 import update_profile
from task4_4 import find_user, book_order, discount_price
from task4_5 import register_user
from task4_7 import payment_book

'''Функция вызова всех функций'''
def call_functions():
    #Вызов функций в заданной последовательности
    print("\nШаг 1:")
    try:
        check_name("a") # Ожидается ошибка без обработки
    except ValueError as pe:
        print(f"Введите возраст больше 18: {pe}")

    try:
        check_age(12) # Ожидается ошибка без обработки
    except PermissionError as ve:
        print(f"Введите имя правильно: {ve}")


    print("\nШаг 2:")
    take_elbook(0) # Обработка ошибки в процессе взятия книги

    print("\nШаг 3:")
    update_profile(1, -10) # Обработка с блоком finally

    print("\nШаг 4:")
    find_user(["danil", "egor", "ilya"], 1) # Ошибка в поиске
    book_order(-10) # Ошибка в заказе
    discount_price(1000, 1000) # Ошибка в скидке

    print("\nШаг 5:")
    register_user("ilya", 18) # Ошибка при регистрации(пользователь уже существует)

    print("\nШаг 7:")
    payment_book(-1, -100) # Ошибка при оплате
# Примеры использования других пользовательских функций прописаны в шаге 4


if __name__ == "__main__":
    call_functions()