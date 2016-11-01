class Person(object):     
    def __init__(self, name):         
        self.name = name     
    def say(self, stuff):
        # print(self.name + ' says: ' + stuff)           
        return self.name + ' says: ' + stuff     
    def __str__(self):
        # print( self.name)           
        return self.name  

class Lecturer(Person):     
    def lecture(self, stuff):
        print( 'lecturer:', 'I believe that ' + Person.say(self, stuff))          
        return 'I believe that ' + Person.say(self, stuff)  

class Professor(Lecturer): 
    def say(self, stuff): 
        print( 'professor', 'Prof. ' + self.name + ' says: ' + self.lecture(stuff))
        return 'Prof. ' + self.name + ' says: ' + self.lecture(stuff)

class ArrogantProfessor(Professor): 
    def say(self, stuff): 
        print('arrogant', self.name + ' says: It is obvious that ' + Person.say(self, stuff))
        return self.name + ' says: It is obvious that ' + Person.say(self, stuff)
    def lecture(self, stuff):
        print( 'It is obvious that ' + Person.say(self, stuff))          
        return 'I believe that ' + Person.say(self, stuff)  
        

e = Person('eric') 
le = Lecturer('eric') 
pe = Professor('eric') 
ae = ArrogantProfessor('eric')

# e.say('the sky is blue')
# eric says: the sky is blue

# le.say('the sky is blue')
# eric says: the sky is blue

# le.lecture('the sky is blue')
# I believe that eric says: the sky is blue

# pe.say('the sky is blue')
# eric says: I believe that eric says: the sky is blue

# pe.lecture('the sky is blue')
# I believe that eric says: the sky is blue

# ae.say('the sky is blue')
# eric says: It is obvious that eric says: the sky is blue

# ae.lecture('the sky is blue')
# It is obvious that eric says: the sky is blue

pe.say('the sky is blue')
# Prof. eric says: I believe that eric says: the sky is blue 

ae.say('the sky is blue')
# Prof. eric says: It is obvious that I believe that eric says: the sky is blue 