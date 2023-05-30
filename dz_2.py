def check_unique_numbers(numbers):
    try:
        if len(numbers) != len(set(numbers)):
            return False
        else:
            return True
    except TypeError:
        raise TypeError("Список повинен містити лише числа")
    except Exception as e:
        raise Exception("Сталася помилка: " + str(e))