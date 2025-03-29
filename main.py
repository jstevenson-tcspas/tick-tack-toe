import random
print ('''
------------   
TIC TACK TOE
------------
''')
p1 = ""
p2 = ""
# list- list of values (variables, integers, strings, etc.)

board = ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"]
# index: 0    1   2   3   4   5   6   7   8
choice = input("X or 0? >")



while choice != "X" and choice != "x" and choice != "0":
    choice = input("Wrong answer. Please choose again> ")

if choice == "X" or choice == "x":
    p1 = "X"
    p2 = "0"
    print('''
------   
Team X 
------
    ''')
elif choice =="0":
    p1 = "0"
    p2 = "X"
    print('''
------
Team 0
------
    ''')

    
def check_winner():
    if board[0] == board[1] and board[0] == board[2] and board[0] != "[ ]":
        return True
    if board[3] == board[4] and board[3] == board[5] and board[3] != "[ ]":
        return True
    if board[6] == board[7] and board[6] == board[8] and board[6] != "[ ]":
        return True
    if board[0] == board[3] and board[0] == board[6] and board[0] != "[ ]":
        return True
    if board[1] == board[4] and board[1] == board[7] and board[1] != "[ ]":
        return True
    if board[2] == board[5] and board[2] == board[8] and board[2] != "[ ]":
        return True
    if board[0] == board[4] and board[0] == board[8] and board[0] != "[ ]":
        return True
    if board[6] == board[4] and board[6] == board[2] and board[6] != "[ ]":
        return True
    return False


    
def grid():
    print("------------------------")
    print(" ".join(board[0:3]))
    print(" ".join(board[3:6]))
    print(" ".join(board[6:9]))
    print("------------------------")

    
grid()

while True:
    pos = int(input("where do you want to place it?\n>"))
    while board[pos] != "[ ]":
        pos = int(input("Please choose an empty position: "))
    board[pos] ="["+p1+"]"
    grid()
    if check_winner() == True:
        print("you win")
        exit()
   
    place = random.randint(0,8)
    while board[place] != "[ ]":
        place = random.randint(0,8)
    board[place] ="["+p2+"]"
    grid()
    if check_winner() == True:
        print("cpu wins")
        exit()
    
    # if board[pos] == "[x] [x] [x]":
    #     print("You win!")
