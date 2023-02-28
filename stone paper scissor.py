import random

# function to compare the input values given by the player and the computer and figure out who's the winner 
def game(x,y):
    print("**********************************************************\n")
    if(x==1):
        if(y==1):
            print("Result : DRAW")
        elif(y==2):
            print("Result : COMPUTER WINS")
        elif(y==3):
            print("Result : YOU WIN")
    elif(x==2):
        if(y==1):
            print("Result : YOU WIN")
        elif(y==2):
            print("Result : DRAW")
        elif(y==3):
            print("Result : COMPUTER WINS")
    elif(x==3):
        if(y==1):
            print("Result : COMPUTER WINS")
        elif(y==2):
            print("Result : YOU WIN")
        elif(y==3):
            print("Result : DRAW")
    print("\n**********************************************************\n")


# DRIVER CODE
m=random.randint(1,3) # take random value as computer's choice

print("\n\n**********************************************************\n")
print("-------------  ~ Stone-paper-scissors game ~  ------------\n")
print("Choose 1 => Stone")
print("       2 => Paper")
print("       3 => Scissiors\n")

ch=int(input("Enter your choice : "))
print("\n")

# show the choices
if(ch==1):
    print("You chose => Stone")
elif(ch==2):
    print("You chose => Paper")
elif(ch==3):
    print("You chose => Scissors")
else:
    print("Invalid choice")
    quit()
    
if(m==1):
    print("Computer chose => Stone")
elif(m==2):
    print("Computer chose => Paper")
elif(m==3):
    print("Computer chose => Scissors") 

game(ch,m) # function call