!/usr/bin/python

class Person(object):     
    def __init__(self, name):         
        self.name = name     
    def say(self, stuff):         
        return self.name + ' says: ' + stuff     
    def __str__(self):         
        return self.name  

class Lecturer(Person):     
    def lecture(self, stuff):         
        return 'I believe that ' + Person.say(self, stuff)  

#6.3 add 'Prof.'
class Professor(Lecturer): 
    def say(self, stuff): 
        return 'Prof. '+self.name + ' says: ' + self.lecture(stuff)
# 6.1
#class ArrogantProfessor(Professor): 
#    def say(self, stuff): 
#        return self.name + ' says: ' + self.lecture(stuff)
#    def lecture(self,stuff):
#        return 'It is obvious that ' + Person.say(self,stuff)
    
# 6.2
class ArrogantProfessor(Professor): 
    def say(self, stuff): 
        return self.name + ' says: ' + self.lecture(stuff)
    def lecture(self,stuff):
        return 'It is obvious that ' + Lecturer.lecture(self,stuff)

