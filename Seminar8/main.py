from os import path

file_base = "directory.txt"
last_id = 0
all_data = []

if not path.exists(file_base):
    with open(file_base, "w", encoding="utf-8") as _:
        pass


def read_records():
    global last_id, all_data

    with open(file_base, encoding="utf-8") as f:
        all_data = [i.strip() for i in f]
        if all_data:
            last_id = int(all_data[-1].split()[0])
            return all_data
    return []


def show_all():
    if all_data:
        print(*all_data, sep="\n")
    else:
        print("Empty data")


# def add_record():
#     with open(file_base, 'a') as fp:
#         fp.write(input('Введите идентификатор: '))
#     with open(file_base, 'a') as fp:
#         fp.write(input('Введите Фамилию : '))
#     with open(file_base, 'a') as fp:
#         fp.write(input('Введите Имя : '))
#     with open(file_base, 'a') as fp:
#         fp.write(input('Введите номер телефона : '))

    




def main_menu():
    play = True
    while play:
        read_records()
        answer = input("Phone book:\n"
                       "1. Show all records\n"
                       "2. Add a record\n"
                       "3. Search a record\n"
                       "4. Change\n"
                       "5. Delete\n"
                       "6. Exp/Imp\n"
                       "7. Exit\n")
        match answer:
            case "1":
                show_all()
            case "2":
                add_record()
            case "3":
                pass
            case "4":
                pass
            case "5":
                pass
            case "7":
                play = False
            case _:
                print("Try again!\n")


main_menu()