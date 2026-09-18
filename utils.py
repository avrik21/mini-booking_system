import os

def clear_terminal():
    os.system("cls")

def click_enter():
    input("Нажмите Enter")

def use_func(func):
    clear_terminal()
    func()
    

def check_number(number):
    try:
        int(number)
        return int(number)
    except ValueError:
        return False

def input_choice(num):
    while True:
        result = check_number(input("Выберите пункт: "))
        if result:
            if result >= 0 and result < num:
                return result
            print("Необходимо выбрать из списка")

def input_lst(num, message):
    while True:
        print(1)
        number = check_number(input(f"{message}"))
        print(2)
        if number <= 1:
            print(3)
            return num

def input_number_tel():
    while True:
        number = input("Введите номер: ")

        if check_number(number):
            if len(number) == 11:
                return int(number)
            print("!!Номер телефона состоит из 11 цифр!!")
            continue
        print("!!Должно быть число!!")
        continue

def input_cost():
    while True:
        number = input("Введите цену: ")
        
        if check_number(number):
            if int(number) > 0:
                return int(number)
            print("!!Цена не может быть меньше 0!!")
            continue
        print("!!Должно быть число!!")
        continue

def input_duration():
    while True:
        number = input("Введите длительность: ")
        
        if check_number(number):
            if int(number) > 0:
                return int(number)
            print("!!Время не может быть меньше 0!!")
            continue
        print("!!Должно быть число!!")
        continue

def get_date():
    while True:
        day = check_number(input("День: "))
        month = check_number(input("Месяц: "))
        year = check_number(input("Год: "))
        if day and month and year:
            break
    return f"{day:02}:{month:02}:{year:04}"
