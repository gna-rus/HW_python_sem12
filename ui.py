from delete_data import delete_row, delete_row_of_number
from change_data import change_row, change_row_of_number_phone
from add_data import add_row, add_row_of_number_phone

from print_data import print_file
from return_data_file import data_file
from choice_file import choice_number_file


def key_from_menu():
    while True:
        key = int(input("Выберите функцию:\n"
                  "1. Добавить\n"
                  "2. Удалить\n"
                  "3. Изменить\n"
                  "4. Содержимое в файлах\n"
                  "5. Выход\n"
                  "Введите номер команды: "))
        if key < 6 and key> 0:
            break
    return key


def check_number(n):
    while n < 1 or n > 5:
        n = key_from_menu()
    return n


def start_menu():
    command = None
    while command != 5:
        nf = choice_number_file()
        command = key_from_menu()
        command = check_number(command)

        if command == 1:
            if nf in [1,2]:
                add_row(nf)
            elif nf == 3:
                add_row_of_number_phone(nf)

        elif command == 2:
            if nf in [1,2]:
                delete_row(nf)
            elif nf == 3:
                delete_row_of_number(nf)

        elif command == 3:
            if nf in [1,2]:
                change_row(nf)
            elif nf == 3:
                change_row_of_number_phone(nf)

        elif command == 4:
            print_file()
    print("Спасибо, что воспользовались нашими услугами!\n"
          "Всего доброго! Приходите к нам ещё :)")