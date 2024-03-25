from return_data_file import data_file
from add_data import format_of_number
from add_data import name_and_surname

def find_row(data):
    count_rows = len(data)
    number_row = int(input(f"Введите номер строки "
                           f"от 1 до {count_rows}: "))
    while number_row < 1 or number_row > count_rows:
        number_row = int(input(f"Ошибка!"
                               f"Введите номер строки "
                               f"от 1 до {count_rows}: "))
    return number_row

def change_row(nf):
    data, nf = data_file(nf)
    number_row = find_row(data)

    surname = input("Введите свою фамилию: ")
    birthdate = input("Введите дату рождения: ")
    town = input("Введите город: ")
    data[number_row - 1] = f'{number_row};{name};{surname};{birthdate};{town}\n'
    with open(f'db/data_{nf}.txt', 'w', encoding='utf-8') as file:
        file.writelines(data)
    print("Данные успешно изменены!")

def change_row_of_number_phone(nf):
    data, nf = data_file(nf)
    number_row = find_row(data)

    name, surname = name_and_surname()
    number = format_of_number()

    data[number_row - 1] = f'{number_row};{name};{surname};{number}\n'
    with open(f'db/data_{nf}.txt', 'w', encoding='utf-8') as file:
        file.writelines(data)
    print("Данные успешно изменены!")
