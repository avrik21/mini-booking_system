from core.appointemt import Appointement

from core.client import Client
from core.service import Service


class System():
    def __init__(self):
        self.clients = []
        self.services = []
        self.appoitments = []

    def add_client(self, name, number):
        for item in self.clients:
            if item.number == number:
                return False
        client = Client(name, number)
        self.clients.append(client)
        print(self.clients, self.services)
        
        return True

    def add_service(self, name, cost, duration):
        for item in self.services:
            if item.name.lower() == name.lower():
                return False
        service = Service(name, cost, duration)
        self.services.append(service)
        print(self.clients, self.services)
        
        return True

    def add_appoitment(self, client, service, date):
        print(self.clients, self.services)
        for item in self.appoitments:
            if item.client == client and item.service == service:
                return False
        appoitment = Appointement(client, service, date)
        appoitment.status = "Запланирована"
        self.appoitments.append(appoitment)
        return True

    def show_appoitments(self):
        info = ""
        for item in self.appoitments:
            info += item.return_info()
        return info

    def find_appoitment(self, name):
        for item in self.appoitments:
            if item.client.name.lower() == name.lower():
                return item
        return False

    def cancel_appoitment(self, name_client, name_service):
        for item in self.appoitments:
            if item.client == name_client.lower() and item.service == name_service.lower():
                item.status == "Отменено"
                return True
        return False

    def change_status(self, name_client, name_service):
        for item in self.appoitments:
            if item.client == name_client.lower() and item.service == name_service.lower():
                item.status == "Выполнено"
                return True

    def income(self):
        result = 0
        for item in self.appoitments:
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
        elif lst == "appoitmesnts":
            for item in self.appoitments:
                print(item.return_info())

    def return_len_lst(self, lst):
        if lst == "clients":
            return len(self.clients)
        elif lst == "services":
            return len(self.services)
        elif lst == "appoitmesnts":
            return len(self.appoitments)

    def return_object(self, lst, num):
        print(lst, num)
        if lst == "clients":
            return self.clients[num]
        elif lst == "services":
            return self.services[num]
        elif lst == "appoitmesnts":
            return self.appoitments[num]

system = System()