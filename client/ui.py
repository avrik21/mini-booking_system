from core.system import system
import utils as ut

class Ui:
    def show_menu(self):
        print("""
Система услуг
===================
1. Добавить клиента
2. Добавить услугу
3. Создать заявку
4. Показать заявки
5. Найти заявку
6. Отменить заявку
7. Изменить статус
8. Прибыль
0. Выход
""")
    
    def request_add_client(self):
        input_name = input("Введите имя: ")
        input_number = ut.input_number_tel()
        result = system.add_client(input_name, input_number)
        if not result:
            print("Пользователь с таким номером уже есть")
            ut.click_enter()
            return
        print("Выполнено!")
        ut.click_enter
        return

    def request_add_service(self):
        input_name = input("Введите название: ")
        input_cost = ut.input_cost()
        input_duration = ut.input_duration()
        result = system.add_service(input_name, input_cost, input_duration)
        if not result:
            print("Услуга с таким названием уже есть")
            ut.click_enter()
            return
        print("Выполнено!")
        ut.click_enter()

    def request_add_appointment(self):
        system.show_info("clients")
        input_client = ut.input_lst(
            system.return_len_lst("clients"), 
            "Введите номер по списку"
            )
        client = system.return_object(
            "clients", 
            input_client-1
            )
        system.show_info("services")
        input_service = ut.input_lst(system.return_len_lst("services"), "Введите номер по списку")
        service = system.return_object("services", input_service-1)
        date = ut.get_date()
        result = system.add_appointment(client, service, date)
        if not result:
            print("Такая заявка уже есть")
            ut.click_enter()
            return
        print("Выполнено!")
        ut.click_enter()
        return

    def request_show_appointments(self):
        result = system.show_appointments()
        if not result:
            print("Список пуст")
            ut.click_enter()
            return
        print(result)
        ut.click_enter()
        return

    def request_find_appoitment(self):
        name_input = input("Что ищете?(Имя) ")
        result = system.find_appoitment(name_input)
        if not result:
            print("Заявка не найдена!")
            ut.click_enter()
            return
        print(result)
        ut.click_enter()
        return

    def request_cancel_appointment(self):
        name_input = input("Имя клиента? ")
        name_service = input("Имя услуги? ")

        result = system.cancel_appointment(name_input, name_service)

        if not result:
            print("Заказ не найден")
            ut.click_enter()
            return

        print("Выполнено!")
        ut.click_enter()
        return

    def request_change_status(self):
        name_input = input("Имя клиента? ")
        name_service = input("Имя услуги? ")

        result = system.change_status(name_input, name_service)
        
        if not result:
            print("Заказ не найден")
            ut.click_enter()
            return

        print("Выполнено!")
        ut.click_enter()
        return

    def request_income(self):
        result = system.income()

        if not result:
            print("Выполненых заказов нет!")
            ut.click_enter()
            return

        print(f"Общая прибыль завершенных заказов {result}руб.")
        ut.click_enter()
        return