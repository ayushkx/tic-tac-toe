import os
import platform

print("\t\t\tWelcome to tic tac toe!!!\n\n")

def clearscreen():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')        

def myboard(b):
    print(b[1]+' | '+b[2]+' | '+b[3])
    print('--+---+--')
    print(b[4]+' | '+b[5]+' | '+b[6])
    print('--+---+--')
    print(b[7]+' | '+b[8]+' | '+b[9])
    print('\n')
    
def userchoice():
    p1 = input('Player1 choose 0 or X: ')
    p1 = p1.upper()
    if p1 == 'X':
        print('Player1: X')
        print('Player2: 0')
        print("start with player1")
        return 2
    elif p1=="0":
        print('Player1: 0')
        print('Player2: X')
        print("start with player1")
        return 3
    else:
        print("Invalid input..please enter valid input")
        userchoice()
        
def gamelogic(b):
    return b[1]==b[2]==b[3] or b[4]==b[5]==b[6] or b[7]==b[8]==b[9] or b[1]==b[4]==b[7] or b[2]==b[5]==b[8] or b[3]==b[6]==b[9] or b[1]==b[5]==b[9] or b[3]==b[5]==b[7]

def userinput(b,p):
    s = input('enter the position: ')
    try:
        k =  int(s)
        if k <=9 and k >= 1 and (b[k] != 'X' and b[k] != '0'):
            b[k] = p
            return p
        else:
            print("please enter the valid position")
            userinput(b,p)
    except:
        print("invalid input")
        userinput(b,p)
        
def start_game():
    while True:
        s = input("Do you want play once again(Y/N): ")
        if s.upper() == "Y":
            return True
        else:
            return False
        
g_count = 0
b = ['','1','2','3','4','5','6','7','8','9']
start = True
k = True

while start:
    myboard(b)
    if userchoice() == 2:
        p1 = 'X'
        p2 = '0'
    else:
        p1 = '0'
        p2 = 'X'
    while g_count < 9:
        if k:
            print("Player1 ")
            win = userinput(b,p1)
            g_count +=1
            k = False
            clearscreen()
        else:
            print("Player2 ")
            win = userinput(b,p2)
            g_count +=1
            k = True
            clearscreen()
        myboard(b)
        if gamelogic(b):
            if win == p1:
                print('Bravo!!! player1 wins...')
                break
            else :
                print('Bravo!!! player2 wins...')
                break
            
    if not gamelogic(b):
        print("Opps..game tied..")
        
    if start_game():
        start = True
        b = ['','1','2','3','4','5','6','7','8','9']
        g_count = 0
        k = True
        clearscreen()
    else:
        start = False
        print("\nThanks for playing!!\n by Ayush ")
        input()
                
