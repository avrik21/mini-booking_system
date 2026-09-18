class Appointement():
    def __init__(self, client, service, date):
        self.client = client
        self.service = service
        self.status = "Новая"
        self.date = date

    def return_info(self):
        return f"""Статус: {self.status} | {self.date}
Клиент: {self.client.name}, {self.client.number}
Услуга: {self.service.name}, {self.service.cost}руб.
"""