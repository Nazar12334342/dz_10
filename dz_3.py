class CustomException(Exception):
    def __init__(self, message, error_code):
        self.message = message
        self.error_code = error_code

    def __str__(self):
        return f"Помилка: {self.message}. Код помилки: {self.error_code}"
