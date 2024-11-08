''' Функция, генерирующая исключения и содержащая обработчики '''

def register_user(username, age):
    """Регистрация пользователя с генерацией и обработкой исключений"""
    user = ["ilya", "danil", "egor"]
    try:
        if not username:
            raise ValueError("имя пользователя не может быть пустым")
        if age < 1:
            raise ValueError("пользователю не может быть меньше 1")
        if username in user:
            raise PermissionError("такой пользователь уже сущевствует")
        print(f"Пользователь {username} успешно зарегистрирован")
    except ValueError as ve:
        print(f"Ошибка{ve}")
    except PermissionError as pe:
        print(f"Ошибка доступа: {pe}")