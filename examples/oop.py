from datetime import date


class Person:
    """Class describing persons"""

    count = 0  # class variable

    def __init__(self, name_param, date_of_birth):
        self.name = name_param  # instance variables
        self.date_of_birth = date_of_birth
        self._increment_count()

    @property
    def age(self):
        return self.compute_age(self.date_of_birth)

    def greet(self, greeting):  # instance method
        print(f'{self.name} says "{greeting}!"')

    @classmethod
    def _increment_count(cls):  # class method
        cls.count += 1

    @staticmethod
    def compute_age(date_of_birth):  # static method
        diff = date.today() - date_of_birth
        return int(diff.days / 365.25)

    def __str__(self):
        return f'{self.__class__.__name__} object (name={self.name})'


class Student(Person):
    count = 0

    def __init__(self, name, university, date_of_birth):
        super().__init__(name, date_of_birth)
        self.university = university

    def greet(self):
        super().greet("Good morning")


class MyClass:
    def __init__(self, **kwargs):
        for key, val in kwargs.items():
            setattr(self, key, val)


if __name__ == '__main__':
    p1 = Person('Anna', date(2001, 5, 7))  # __init__ is executed

    print('Number of persons:', Person.count)

    p2 = Person('John', date(1986, 2, 23))
    print(p1.name, p2.name)

    print('Number of persons:', Person.count)

    print('Class attributes can be accessed from instances:',
          p1.count is Person.count)

    p1.greet('Hello')
    p2.greet('Hi')

    Person._increment_count()
    print('Number of persons:', Person.count)
    print(Person.compute_age(date(1999, 3, 1)))

    p1._increment_count()
    print('Number of persons:', Person.count)

    print(p1.compute_age(date(2006, 3, 1)))

    print(p1, str(p1), repr(p1))

    print(f"{p1.name}'s age is {p1.age}.")

    s1 = Student('Mike', 'ASE', date(2003, 2, 23))
    s1.greet()
    print(s1, s1.university, s1.age)

    print(Student.count, Person.count)

    person = MyClass(name='Jane', age=15, height=1.5)
    print(person.name, person.age, person.height)

    dog = MyClass(name='Bobby', owner=person)
    print(dog.name, dog.owner.name)
