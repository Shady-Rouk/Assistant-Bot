import random

field = [
    ["", "", ""],
    ["", "", ""],
    ["", "", ""]
]
won = False
winner = ""

def fieldFull():
    count = 0
    for i in field:
        for j in i:
            if j != "":
                count += 1
    if count == 9:
        return True
    return False


def determineWin():
    global winner
    if (field[0][0] == field[0][1] and field[0][0] == field[0][2] and field[0][0] == "X") or (field[1][0] == field[1][1] and field[1][0] == field[1][2] and field[1][0] == "X") or (field[2][0] == field[2][1] and field[2][0] == field[2][2] and field[2][0] == "X"):
        winner = "You"
        return True
    elif (field[0][0] == field[0][1] and field[0][0] == field[0][2] and field[0][0] == "O") or (field[1][0] == field[1][1] and field[1][0] == field[1][2] and field[1][0] == "O") or (field[2][0] == field[2][1] and field[2][0] == field[2][2] and field[2][0] == "O"):
        winner = "Comp"
        return True
    elif (field[0][0] == field[1][0] and field[0][0] == field[2][0] and field[0][0] == "X") or (field[0][1] == field[1][1] and field[0][1] == field[2][1] and field[0][1] == "X") or (field[0][2] == field[1][2] and field[0][2] == field[2][2] and field[0][2] == "X"):
        winner = "You"
        return True
    elif (field[0][0] == field[1][0] and field[0][0] == field[2][0] and field[0][0] == "O") or (field[0][1] == field[1][1] and field[0][1] == field[2][1] and field[0][1] == "O") or (field[0][2] == field[1][2] and field[0][2] == field[2][2] and field[0][2] == "O"):
        winner = "Comp"
        return True
    elif (field[0][0] == field[1][1] and field[0][0] == field[2][2] and field[0][0] =="X") or (field[0][2] == field[1][1] and field[0][2] == field[2][0] and field[0][2] == "X"):
        winner = "You"
        return True
    elif (field[0][0] == field[1][1] and field[0][0] == field[2][2] and field[0][0] =="O") or (field[0][2] == field[1][1] and field[0][2] == field[2][0] and field[0][2] == "O"):
        winner = "Comp"
        return True
    return False


#check turns, make sure each player plays

while(not won):
    choice = input("r, c: ")
    cPlay = False
    choice = choice.split(" ")
    r = int(choice[0])
    c = int(choice[1])
    
    if(field[r][c] != "O") and (field[r][c] == ""):
        field[r][c] = "X"

    if determineWin():
        print(winner, "won!")
        won = True
        break

    if fieldFull() and not won:
        print("It's a tie!!")
        break

    while(not cPlay):
        compR = random.randint(0, 2)
        compC = random.randint(0, 2)
        if(field[compR][compC] != "X") and (field[compR][compC] == ""):
            field[compR][compC] = "O"
            cPlay = True

    for row in field:
        print(row)    

    if determineWin():
        print(winner, "won!")
        won = True
        break

        

