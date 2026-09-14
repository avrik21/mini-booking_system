class Appointement():
    def __init__(self, client, service, date_and_time):
        self.client = client
        self.service = service
        self.status = "Новая"

    def return_info(self):
        return f"""Статус: {self.status}
Клиент: {self.client.name}, {self.client.number}
Услуга: {self.service.name}, {self.service.cost}руб.
"""