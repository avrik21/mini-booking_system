def input_number(max_num, min_num = 0):
    try:
        number = int(input("Введите номер"))
    except ValueError:
        print("Только число")