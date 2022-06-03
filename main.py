from ast import Return
from pydoc import text
import random
from unittest import result





def User():
    valid_input=False
    while valid_input==False:
        userinput=input("Choose and Input a letter between R, P or S ensure you make one choice: \n")
        if userinput=="R":
            valid_input=True
            print("USER INPUT: R")
        elif userinput=="P":
            valid_input=True
            print("USER INPUT: P")
        elif userinput=="S":
            valid_input=True
            print("USER INPUT: S")

        
        else:
            print("fuck up")
    Computer(userinput)
        

    
        


        
def Computer(rest):
    tiles=["R","P","S"]

    result=random.choice(tiles)
    print("COMPUTER INPUT: ",result)
    
    

    text=rest
    
    
    if text==result:
        print("tile, please repeat")
        User()
    elif text=="R" and result=="S":
        print("USER  WINS  USER  WINS  USER  WINS  USER  WINS  USER  WINS")
        print("player: ",text, "      :    " "CPU: ", result)
        print("R-----Rock\nS-----Scissors\nP-----Paper")
    elif text=="S" and result=="P":
        print("USER  WINS  USER  WINS  USER  WINS  USER  WINS  USER  WINS")
        print("player: ",text, "      :    " "CPU: ", result)
        print("R-----Rock\nS-----Scissors\nP-----Paper")
    elif text=="P" and result=="R":
        print("USER  WINS  USER  WINS  USER  WINS  USER  WINS  USER  WINS")
        print("player: ",text, "      :    " "CPU: ", result)
        print("R-----Rock\nS-----Scissors\nP-----Paper")

    else:
        
        print("COMPUTER WINS  COMPUTER WINS  COMPUTER WINS  COMPUTER WINS")
        print("player: ",text, "      :    " "CPU: ", result)
        print("R-----Rock\nS-----Scissors\nP-----Paper")


User()
   





    
    







    


