from core.appointment import Appointment

from core.client import Client
from core.service import Service


class System():
    def __init__(self):
        self.clients = []
        self.services = []
        self.appointments = []

    def add_client(self, name, number):
        for item in self.clients:
            if item.number == number:
                return False
        client = Client(name, number)
        self.clients.append(client)
        return True

    def add_service(self, name, cost, duration):
        for item in self.services:
            if item.name.lower() == name.lower():
                return False
        service = Service(name, cost, duration)
        self.services.append(service)
        
        return True

    def add_appointment(self, client, service, date):
        for item in self.appointments:
            if item.client == client and item.service == service:
                return False
        appointment = Appointment(client, service, date)
        appointment.status = "Запланирована"
        self.appointments.append(appointment)
        return True

    def show_appointments(self):
        info = ""
        for item in self.appointments:
            info += item.return_info()
        return info

    def find_appointment(self, name):
        for item in self.appointments:
            if item.client.name.lower() == name.lower():
                return item
        return False

    def cancel_appointment(self, name_client, name_service):
        for item in self.appointments:
            if item.client.name.lower() == name_client.lower() and item.service.name.lower() == name_service.lower():
                item.status = "Отменено"
                return True
        return False

    def change_status(self, name_client, name_service):
        for item in self.appointments:
            if item.client.name.lower() == name_client.lower() and item.service.name.lower() == name_service.lower():
                item.status = "Выполнено"
                return True
        return False

    def income(self):
        result = 0
        for item in self.appointments:
            if item.status == "Выполнено":
                result += item.service.cost
        return result

    def show_info(self, lst):
        if lst == "clients":
            for item in self.clients:
                print(item.return_info())
        elif lst == "services":
            for item in self.services:
                print(item.return_info())
        elif lst == "appointments":
            for item in self.appointments:
                print(item.return_info())

    def return_len_lst(self, lst):
        if lst == "clients":
            return len(self.clients)
        elif lst == "services":
            return len(self.services)
        elif lst == "appointments":
            return len(self.appointments)

    def return_object(self, lst, num):
        if lst == "clients":
            return self.clients[num]
        elif lst == "services":
            return self.services[num]
        elif lst == "appointments":
            return self.appointments[num]

system = System()