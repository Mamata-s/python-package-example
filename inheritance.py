


class Person(object):
    def __init__(self,name):
        self.name=name
        print('person init callled')


    def display(self):
        print('the name is ',self.name)
    

class Student(Person):
    def __init__(self, name,id):
        super().__init__(name)
        self.id = id

    def display(self):
        print('name of student is',self.name)
        print('id no of student is ',self.id)



a= Student('Mamata',10547)
a.display()