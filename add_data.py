from return_data_file import data_file


def name_and_surname():
    name = input("Введите свое имя: ")
    surname = input("Введите свою фамилию: ")
    return name, surname

def format_of_number():
    while True:
        number = input("Введите номер телефона (десятизначный и без разделителей): ")
        if number.isdigit():
            real_number = f'8({number[-10:-7]}){number[-7:-4]}-{number[-4:-2]}-{number[-2:]}' # такая форма на случай если номер будет не стандартным (номер может быть локальным)
            break
    return real_number

def add_row(nf):
    name, surname = name_and_surname()
    birthdate = input("Введите дату рождения: ")
    town = input("Введите город: ")
    data, nf = data_file(nf)
    now_number_row = len(data) + 1
    with open(f'db/data_{nf}.txt', 'a', encoding='utf-8') as file:
        file.write(f'{now_number_row};{name};'
                   f'{surname};{birthdate};{town}\n')
    print("Данные успешно записаны!")


def add_row_of_number_phone(nf):
    name, surname = name_and_surname()
    number = format_of_number()
    data, nf = data_file(nf)
    now_number_row = len(data) + 1
    with open(f'db/data_{nf}.txt', 'a', encoding='utf-8') as file:
        file.write(f'{now_number_row};{name};'
                   f'{surname};{number}\n')
    print("Данные успешно записаны!")