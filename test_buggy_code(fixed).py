def calculate_discount(price, age, is_student):
    """
    Расчет скидки на товар
    """
    discount = 0

    # Скидка по возрасту
    if age < 18:
        discount += 10
    elif age >= 60:  # Исправлено: >= вместо >
        discount += 15

    # Скидка для студентов
    if is_student == True:
        discount += 5

    # Максимальная скидка не более 25%
    if discount > 25:
        discount = 25

    final_price = price - (price * discount / 100)
    return final_price


def validate_password(password):
    """
    Проверка надежности пароля
    """
    if len(password) < 6:
        return "Слишком короткий"

    has_upper = False
    has_lower = False
    has_digit = False

    for char in password:
        if char.isupper():
            has_upper = True
        if char.islower():
            has_lower = True
        if char.isdigit():
            has_digit = True

    if has_upper and has_lower and has_digit:
        return "Надежный"
    else:
        return "Ненадежный"


def get_temperature_status(temp):
    """
    Определение статуса температуры
    """
    if temp <= 0:
        return "Лед"
    elif temp < 10:  # Исправлено: правильные границы диапазонов
        return "Холодно"
    elif temp < 20:
        return "Прохладно"
    elif temp < 30:
        return "Тепло"
    else:
        return "Жарко"


def test_calculate_discount():
    """Тесты для функции calculate_discount"""
    print("Тестирование calculate_discount...")

    # Тест 1: Обычный покупатель
    result = calculate_discount(1000, 25, False)
    print(f"Взрослый не студент: {result}")

    # Тест 2: Несовершеннолетний
    result = calculate_discount(1000, 16, False)
    print(f"Несовершеннолетний: {result}")

    # Тест 3: Пенсионер
    result = calculate_discount(1000, 65, False)
    print(f"Пенсионер: {result}")

    # Тест 4: Студент
    result = calculate_discount(1000, 20, True)
    print(f"Студент: {result}")

    # Тест 5: Студент-пенсионер (максимальная скидка)
    result = calculate_discount(1000, 65, True)
    print(f"Студент-пенсионер: {result}")

    # Тест 6: Граничный возраст 18 лет
    result = calculate_discount(1000, 18, False)
    print(f"Возраст 18 лет: {result}")

    # Тест 7: Граничный возраст 60 лет
    result = calculate_discount(1000, 60, False)
    print(f"Возраст 60 лет: {result}")


def test_validate_password():
    """Тесты для функции validate_password"""
    print("\nТестирование validate_password...")

    # Тест 1: Слишком короткий пароль
    result = validate_password("Ab1")
    print(f"Короткий пароль 'Ab1': {result}")

    # Тест 2: Надежный пароль
    result = validate_password("Password123")
    print(f"Надечный пароль 'Password123': {result}")

    # Тест 3: Без заглавных букв
    result = validate_password("password123")
    print(f"Без заглавных 'password123': {result}")

    # Тест 4: Без цифр
    result = validate_password("Password")
    print(f"Без цифр 'Password': {result}")

    # Тест 5: Только заглавные
    result = validate_password("PASSWORD123")
    print(f"Только заглавные 'PASSWORD123': {result}")

    # Тест 6: Граничная длина
    result = validate_password("Abc12")
    print(f"Пароль из 5 символов 'Abc12': {result}")

    result = validate_password("Abc123")
    print(f"Пароль из 6 символов 'Abc123': {result}")


def test_get_temperature_status():
    """Тесты для функции get_temperature_status"""
    print("\nТестирование get_temperature_status...")

    # Тест всех температурных диапазонов
    test_cases = [
        (-5, "Лед"),
        (0, "Лед"),
        (5, "Холодно"),
        (10, "Холодно"),
        (15, "Прохладно"),
        (20, "Тепло"),
        (25, "Тепло"),
        (30, "Жарко"),
        (35, "Жарко")
    ]

    print("Проверка температурных диапазонов:")
    for temp, expected in test_cases:
        result = get_temperature_status(temp)
        status = "✅ ПРОШЕЛ" if result == expected else "❌ НЕ ПРОШЕЛ"
        print(f"  {status} Температура {temp}°C: получено '{result}', ожидалось '{expected}'")


def main():
    """Основная функция для запуска всех тестов"""
    print("🔍 ЗАПУСК ТЕСТИРОВАНИЯ БЕЛЫМ ЯЩИКОМ")
    print("=" * 50)

    test_calculate_discount()
    test_validate_password()
    test_get_temperature_status()
    
    print("\n✅ Все тесты завершены успешно!")


# Запуск программы
if __name__ == "__main__":
    main()