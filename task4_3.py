''' Функция с общим обработчиком исключений exception и блоком finally '''

def update_profile(user_id, age):
    """Обновление профиля пользователя с обработчиком и блоком finally"""
    try:
        if age < 0:
            raise ValueError("возраст не может быть отрицательным")
        print(f"Профиль пользователя {user_id} обновлен. Новый возраст {age}")
    except Exception as e:
        print(f"Ошибка при обновлении пользователя: {e}")
        return False
    finally:
        print("Профиль обновлен, если возраст больше 0")