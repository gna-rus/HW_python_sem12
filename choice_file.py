from print_data import print_file


def choice_number_file():
    print_file()
    number = int(input("Выберит файл, с которым Вы хотите работать\n"
                       "Введите цифру 1,2 или 3: "))
    while number < 1 or number > 3:
        number = int(input("Ошибка!!!\n"
                           "Введите цифру 1,2 или 3: "))
    return number
