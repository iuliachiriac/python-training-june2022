from datetime import date


class Person:
    """Class describing persons"""

    count = 0  # class variable

    def __init__(self, name):
        self.name = name  # instance variables
        Person.count += 1

    def greet(self, greeting):  # instance method
        print(f'{self.name} says "{greeting}!"')

    @classmethod
    def increment_count(cls):  # class method
        cls.count += 1

    @staticmethod
    def compute_age(date_of_birth):  # static method
        diff = date.today() - date_of_birth
        return int(diff.days / 365.25)


if __name__ == '__main__':
    p1 = Person('Anna')  # __init__ is executed

    print('Number of persons:', Person.count)

    p2 = Person('John')
    print(p1.name, p2.name)

    print('Number of persons:', Person.count)

    print('Class attributes can be accessed from instances:',
          p1.count is Person.count)

    p1.greet('Hello')
    p2.greet('Hi')

    Person.increment_count()
    print('Number of persons:', Person.count)
    print(Person.compute_age(date(1999, 3, 1)))

    p1.increment_count()
    print('Number of persons:', Person.count)

    print(p1.compute_age(date(2006, 3, 1)))
