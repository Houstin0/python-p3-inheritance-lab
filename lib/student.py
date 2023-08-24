#!/usr/bin/env python

from user import User

class Student(User):

    def __init__(self, first_name, last_name,knowledge=[]):
        self.knowlegde=knowledge
        super().__init__(first_name, last_name)
    
    def learn(self,new_information):
        self.knowlegde.append(new_information)

john=Student("john","doe")
print(hasattr(john,"knowlegde"))