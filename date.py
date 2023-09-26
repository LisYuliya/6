# Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
# Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
# Для простоты договоримся, что год может быть в диапазоне[1, 9999].
# Весь период(1 января 1 года - 31 декабря 9999 года)  действует Григорианский календарь.
# Проверку года на високосность вынести в отдельную защищённую функцию.

# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.

import sys


def is_leap_year(year):

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False


def is_valid_date(date_str):

    parts = date_str.split('.')

    if len(parts) != 3:
        return False

    day, month, year = map(int, parts)

    if year < 1 or year > 9999:
        return False

    if month < 1 or month > 12:
        return False

    if month in [4, 6, 9, 11] and (day < 1 or day > 30):
        return False

    if month == 2:
        if is_leap_year(year):
            if day < 1 or day > 29:
                return False
        else:
            if day < 1 or day > 28:
                return False

    if day < 1 or day > 31:
        return False

    return True


if __name__ == "__main__":

    date = '29.02.2025'
    if is_valid_date(date):
        print(f"Дата {date} действительна")
    else:
        print(f"Дата {date} недействительна")

    if len(sys.argv) != 2:
        print("Для проверки другой даты, пожалуйста, укажите в терминале дату в формате DD.MM.YYYY")
    else:
        date = sys.argv[1]
        if is_valid_date(date):
            print(f"Дата {date} действительна")
        else:
            print(f"Дата {date} недействительна")
