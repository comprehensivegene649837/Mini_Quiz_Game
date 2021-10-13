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
print(f' total points = : {points}')





 
















