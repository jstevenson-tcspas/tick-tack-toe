print ('''
------------   
TIC TACK TOE
------------
''')
p1 = ""
p2 = ""
# list- list of values (variables, integers, strings, etc.)

board = ["", "", "", "", "", "", "", "", ""]
# index: 0    1   2   3   4   5   6   7   8

choice = input("X or 0? >")
if choice == "X":
    p1 = "X"
    p2 = "0"
    print('''
------   
Team X 
------
    ''')
elif choice == "0":
    p1 = "0"
    p2 = "X"
    ('''
------
Team 0
------
    ''')
print("------------------------")
