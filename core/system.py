from client import Client
from service import Service
from appointemt import Appointement

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
        return True

    def add_service(self, name, cost, duration):
        for item in self.services:
            if item.name.lower() == name.lower():
                return False
        service = Service(name, cost, duration)
        self.services.append(service)
        return True

    def add_appoitment(self, client, service, date_and_time):
        for item in self.appoitments:
            if item.date_and_time == date_and_time:
                return False
        appoitment = Appointement(client, service, date_and_time)
        appoitment.status = "Запланирована"
        self.appoitments.append(appoitment)
        return True

    def show_appoitments(self):
        for item in self.appoitments:
            return item.return_info()
        return False

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

system = System()