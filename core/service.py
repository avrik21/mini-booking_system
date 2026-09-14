class Service:
    def __init__(self, name, cost, duration):
        self.name = name
        self.cost = cost
        self.duration = duration

        def return_info(self):
            return f"Услуга: {self.name} | Стоимость: {self.cost} | На {duration}час."