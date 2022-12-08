#stone paper scissor game
import random
def gamewin(comp,user): #this is a gamewin function which calculates who won , constructed this 2nd
    if comp==user:
        return None #if the value chose by the comp and user is same , its a none and game is tie
    elif(comp=='s'): #here the comp chose s that means stone
        if(user=='p'): #user chose paper
            return True # so its obvious that user will win in this case
        elif(user=='sc'): # user chose scissor
            return False # user looses here 
    elif(comp=='p'):
        if(user=='s'):
            return False
        elif(user=='sc'):
            return True
    elif(comp=='sc'):
        if(user=='s'):
            return True
        elif(user=='p'):
            return False
print("Computer's Turn : Stone(s),Paper(p),Scissor(sc) ??\n") #constructed this part first as i used 
# a random function which allows the computer to take its chance first and randomly chooses a value
#so that i wont be able to know which value did computer chose from stone paper or scissor
randomno=random.randint(1,3) #randint(1,3) helps the computer to choose values from 1,2 and 3
if(randomno==1): 
    comp='s'
elif(randomno==2):
    comp='p'
elif(randomno==3):
    comp='sc'

user=input("Now it's your turn : Stone(s),Paper(p),Scissor(sc) ?? \n")


winloose=gamewin(comp,user)
print(f"comp chose {comp}") # this will show what comp has choosen
print(f"user chose {user}") # this will reflect what user has entered

# here i have declared that in what conditions game is going to get tied , won by the user 
# and lost by the user
if winloose==None:
    print("The game tied.\n Thank you for playing asshole")
elif winloose==True:
    print("You win , nice game")
elif winloose==False:
    print("You loose, better luck next time motherfucker")

