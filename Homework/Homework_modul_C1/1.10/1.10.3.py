class Clients:
    def __init__(self, name='Не указано', balance='Нет информации'):
        self.name = name
        self.balance = balance

    def change_balance(self, value=0):
        self.balance += value

    def get_information(self):
        return 'Клиент: {name}.\nБаланс: {balance}.'.format(name=self.name, balance=self.balance)


Ivan = Clients("Иван", 100)
Nikolya = Clients("Николя", 53)
Max = Clients("Максим", 89)

Ivan.change_balance(50)
print(Ivan.get_information())
