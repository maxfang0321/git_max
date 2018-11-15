class Student(object):
    count = 0
    def __init__(self,name,score):
        self.__name = name
        self.__score = score
        Student.count += 1

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self,score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

    def print_score(self):
        print('%s:%s' % (self.__name, self.__score))

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'

class Animal(object):
    def run(self):
        print('Animal is Runnig')

class Dog(Animal):
    def eat(self):
        print('Dog eat quick')

class Cat(Animal):
    def eat(self):
        print('Cat eat slow')
