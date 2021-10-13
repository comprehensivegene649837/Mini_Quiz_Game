#class QuizGame:
#    
#    def __init__(self, s, r):
#        self.s= s
#        self.r= r
#    
#    def getInfo(self):
#        if self.s == "yes":
#            return "hurray! you got one point"
#    
#        elif self.s== "no":
#            return "sorry! you lost"
#    
#        else: #self.s!= "yes" or self.r!= "no":
#            return "invalid input!"
#
#   
#
#    def rectangle(self):
#        if self.r== ("length*breadth") or self.r==("breadth*length"):
#                return "hurray! you got one point"
#
#        else:  #self.r!= ("length*breadth") or self.r!=("breadth*length"):
#            return"invalid input!"
#    
#
#
#
#
#o= input("is the Earth spherical in shape:  ")
#j= input("What is the area of rectangle: ")
#a= QuizGame(o, j)
#print(a.getInfo())
#print(a.rectangle())

import random

print("Is the earth spherical in shape: ")
points= 0

def adjustPoints(p = 1):
  global points
  points += p

def quizGame(s): #to make the first question
    
    if s == "yes":
        adjustPoints(1)
            
        new= ("hurray! you got 1 point", "Awesome! Move ahead!")
        randomn = random.choice(new)     
        return randomn
            
        
    
    
    elif s== "no": 
       
        
        adjustPoints(0)
        
        new = ("better luck next time!" , "oops! wrong answer")
        randomn = random.choice(new)
    
    else: 
        
        return "invalid input!"



def quizGame2(a): #to make the second question
    

    if a== ("l*b") or a==("b*l"):
        adjustPoints(1)
        new= ("hurray! you got 1 point", "Well Done!")
        randomn = random.choice(new)     
        return randomn
    else:
        
        adjustPoints(0)

        new = ("better luck next time!" , "Sorry! wrong answer")
        randomn = random.choice(new)
        
        return randomn
    

print(quizGame(input("enter your answer: "))) #input the first answer 
print(quizGame2(input("what is the area of rectangle: "))) #input the second answer
#def quizGame()
#def quizGame2()
print(f' total points = : {points}')





 
















