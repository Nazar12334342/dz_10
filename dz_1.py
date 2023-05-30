def get_month_name(month_number):
    try:
        months = {
            1: "Січень",
            2: "Лютий",
            3: "Березень",
            4: "Квітень",
            5: "Травень",
            6: "Червень",
            7: "Липень",
            8: "Серпень",
            9: "Вересень",
            10: "Жовтень",
            11: "Листопад",
            12: "Грудень"
        }
        return months[month_number]
    except KeyError:
        print("Невірний номер місяця")
    except TypeError:
        print("Введіть ціле число")

month_number = 3
month_name = get_month_name(month_number)
print(month_name)
