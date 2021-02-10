class Cat:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def show_name(self):
        return 'Имя кота: {}'.format(self.name)

    def show_gender(self):
        return 'Пол кота: {}'.format(self.gender)

    def show_age(self):
        return 'Возраст кота: {}'.format(self.age)
