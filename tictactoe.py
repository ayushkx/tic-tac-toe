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
    global computer

    choice = 0

    while True:
        p1 = input('Player1 choose O or X: ')
        p1 = p1.upper()
        if p1 == 'X':
            print('Player1: X')
            print('Player2: O')
            print("start with player1")
            choice = 2
            break
        elif p1=="O":
            print('Player1: O')
            print('Player2: X')
            print("start with player1")
            choice = 3
            break
        else:
            print("Invalid input..please enter valid input")

    vs_comp = ''
    while True:
        vs_comp = input("Want to play against computer? (Y/N)")
        if vs_comp.upper()=='Y' : 
            computer = True
            break
        if vs_comp.upper()=='N' : 
            computer = False
            break
        print("Invalid Choice. Type either 'y' or 'n'")

    return choice

        
def gamelogic(b):
    return b[1]==b[2]==b[3] or b[4]==b[5]==b[6] or b[7]==b[8]==b[9] or b[1]==b[4]==b[7] or b[2]==b[5]==b[8] or b[3]==b[6]==b[9] or b[1]==b[5]==b[9] or b[3]==b[5]==b[7]

def userinput(b,p):
    global computer, p2
    if computer and p2==p:
        #AI here
        mx = 0
        b2 = [0]*10
        for i in range(1,10):
            if b[i] == p1 : b2[i] = 1
            if b[i] == p2 : b2[i] = -1
        mx = max(b2[1]+b2[2]+b2[3], max(b2[4]+b2[5]+b2[6], b2[7]+b2[8]+b2[9]))
        mx = max(mx, max(b2[1]+b2[4]+b2[7], max(b2[2]+b2[5]+b2[8], b2[3]+b2[6]+b2[9])))
        mx = max(mx, max(b2[1]+b2[5]+b2[9], b2[3]+b2[5]+b2[7]))

        d = {1:[1,3,4], 2:[3], 3:[3, 2], 4:[1], 7:[1]}
        for i1 in d:
            for i2 in d[i1]:
                if mx == (b2[i1]+ b2[i1+i2] + b2[i1+i2*2]):
                    if b2[i1] == 0:
                        b[i1] = p
                        return p
                    if b2[i1+i2*2] == 0: #give more priority to corner
                        b[i1+i2*2] = p
                        return p
                        break
                    if b2[i1+i2] == 0:
                        b[i1+i2] = p
                        return p
                        break

        return p


    s = input('enter the position: ')
    try:
        k =  int(s)
        if k <=9 and k >= 1 and (b[k] != 'X' and b[k] != 'O'):
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
computer = False
b = ['','1','2','3','4','5','6','7','8','9']
start = True
k = True

while start:
    myboard(b)
    if userchoice() == 2:
        p1 = 'X'
        p2 = 'O'
    else:
        p1 = 'O'
        p2 = 'X'
    while g_count < 9:
        if k:
            print("Player1 ")
            win = userinput(b,p1)
            g_count +=1
            k = False
            clearscreen()
        else:
            if computer:
                print("Computer ")
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
                if computer:
                    print('Yay!!  I (computer) win!!')
                else:
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
                
