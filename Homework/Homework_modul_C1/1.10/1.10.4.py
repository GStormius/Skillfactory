# Информация о людях, которые могут стать гостями мероприятия
class Person:
    def __init__(self, firstname='Не указано', lastname='Не указано', city='Не указано', status='Не указано'):
        self.firstname = firstname
        self.lastname = lastname
        self.city = city
        self.status = status

    #  Перевод информации о госте в формат словаря для добавления в список приглашенных
    def add_to_list_guest(self):
        return {'Имя': self.firstname, 'Фамилия': self.lastname, 'Город': self.city, 'Статус': self.status}

    #  Получить информацию о госте
    def get_information(self):
        return 'Информация о госте: {} {}, {}, {}'.format(self.firstname, self.lastname, self.city, self.status)


#  Создание мероприятия
class Event:
    guests = []

    def __init__(self, title):
        self.title = title

    def add_guest(self, guest):
        return Event.guests.append(guest)


halloween = Event('Halloween')
guest_1 = Person('Петр', 'Александров', 'Москва', 'Волонтер')
guest_2 = Person('Максим', 'Филимонов', 'Санкт-Петербург', 'Наставник')
guest_3 = Person('Алексей', 'Павленко', 'Москва', 'Волонтер')

halloween.add_guest(guest_1.add_to_list_guest())

print(halloween.guests)
