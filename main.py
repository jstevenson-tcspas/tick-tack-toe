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
def check_winner(symbol):
    win_patterns= [
        [0, 1, 2], [3, 4, 5],[6, 7, 8]
    ]
def grid():
    print("------------------------")
    print(" ".join(board[0:3]))
    print(" ".join(board[3:6]))
    print(" ".join(board[6:9]))
    print("------------------------")

    
grid()

while True:
    pos = int(input("where do you want to place it?\n>"))
    if board[pos] == "[ ]":
        board[pos] ="["+p1+"]"
    grid()
    place = random.randint(0,8)
    board[place] ="["+p2+"]"
    grid()
    # if board[pos] == "[x] [x] [x]":
    #     print("You win!")

    
