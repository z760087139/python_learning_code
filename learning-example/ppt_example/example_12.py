class Human():
    type = 'human'
    def __init__(self,name,age):
        print('step 1')
        self.name = name
        self.age = age
        self.__change_name()
    
    def __change_name(self):
        self.name = 'No one'

    @classmethod
    def change_type(cls):
        cls.type = 'student'

    @staticmethod
    def count(x,y):
        return x+y

class Boy(Human):
    def __init__(self,name,age):
        super().__init__(name,age)
        print('step 2')
        self.age *= 2

class Student(Human):
    def __init__(self,name,age):
        super().__init__(name,age)
        print('step 3')
        self.age += 2

# 钻石问题
class BStudent(Student,Boy):
    def __init__(self,name,age):
        Student.__init__(self,name,age)
        Boy.__init__(self,name,age)
        # super().__init__(name,age)

# mix-in
class Age():
    def get_age(self):
        return self.age

class Final(BStudent,Age):
    pass

t = BStudent('t',10)
f = Final('t',10)