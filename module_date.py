def is_leap(year: int) -> bool:
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True


def check_date(date: str) -> bool:
    day, month, year = map(int, date.split('.'))
    if year < 1 or year > 9999:
        return False
    if month < 1 or month > 12:
        return False
    if day < 1:
        return False
    if month == 2:
        if is_leap(year):
            if day > 29:
                return False
        elif day > 28:
            return False
    elif month in [4, 6, 9, 11]:
        if day > 30:
            return False
    else:
        if day > 31:
            return False
    return True

if __name__ == "__main__":
    date = input("Введите дату в формате dd.mm.yyyy: ")
    if check_date(date):
        print("Дата валидна")
    else:
        print("Дата невалидна")