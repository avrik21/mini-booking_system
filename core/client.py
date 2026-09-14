class Client():
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def return_info(self):
        return f"Клиент: {self.name} | Номер: {self.number}."