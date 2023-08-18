from module_date import check_date

date = input('Введите дату в формате DD.MM.YYYY: ')
if check_date(date):
    print('Такая дата существует')
else:
    print('Такой даты нет')