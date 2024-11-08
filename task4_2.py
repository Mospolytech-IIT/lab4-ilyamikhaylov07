'''Функция с одним обработчиком исключения общего типа, принимающая один или несколько параметров'''
def take_elbook(amount):
    """Процесс взятия электронной книги"""
    try:
        if amount <= 0:
            raise ValueError("Вы не можете взять 0 книг.")
        print(f"Спасибо, за взятие {amount} книг")
    except Exception as e:
        print(f"Ошибка при взятии книг {e}")
        amount = 0 # Сбрасываем
        return False