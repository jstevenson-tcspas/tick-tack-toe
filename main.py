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
choice = input("X or O? >")

while choice != "X" and choice != "x" and choice != "O":
    choice = input("Wrong answer. Please choose again> ")

if choice == "X" or choice == "x":
    p1 = "X"
    p2 = "O"
    print('''
------   
Team X 
------
    ''')
elif choice =="O":
    p1 = "O"
    p2 = "X"
    print('''
------
Team O
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
cpu_score = 0
player_score = 0

    
def grid():
    print("------------------------")
    print(" ".join(board[0:3]))
    print(" ".join(board[3:6]))
    print(" ".join(board[6:9]))
    print("------------------------")

    
grid()

while cpu_score < 5 and player_score < 5:
    pos = input("where do you want to place it?\n>")
    while pos not in "012345678" or len(str(pos)) != 1:
        pos = input("Please choose a valid answer: ")

    while board[int(pos)] != "[ ]":
        pos = int(input("Please choose an empty position: "))
    board[int(pos)] ="["+p1+"]"
    grid()
    if check_winner() == True:
        print("you win")
        player_score += 1
        board = ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"]
    if "[ ]" not in board:
        print("you drawed")
        board = ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"]
    place = random.randint(0,8)
    while board[place] != "[ ]":
        place = random.randint(0,8)
    board[place] ="["+p2+"]"
    grid()
    if check_winner() == True:
        print("cpu wins")
        cpu_score += 1
        board = ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"]
    if "[ ]" not in board:
        print("you drawed")
        board = ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"]
    
    print(cpu_score, player_score)
    
print('''                            Final scores!
                -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -
    
                                        player_score:{}
                -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -
                                        cpu_score:{}
                -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -
            
    '''.format(player_score, cpu_score))