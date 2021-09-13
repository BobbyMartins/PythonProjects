player1_score = 0  # Global score variables for user information
player2_score = 0


def display(row1, row2, row3):
    """
    :param row1: List[string]
    :param row2: List[string]
    :param row3: List[string]
    :return: null

    function to display tic-tac-toe grid
    """
    print(row1)
    print(row2)
    print(row3)


def check(s):
    """
    :param s: string
    :return: List[int]

    function to check if userInput is valid
    """
    if len(s) != 3 or "," not in s:  # returns false if length of s less than 3 or if separator is not present
        return False
    try:
        row, column = int(s[0]), int(s[2])  # checks if number was used for inputs
    except ValueError:
        return False

    return [row, column] if 1 <= row <= 3 and 1 <= column <= 3 else False


def space_check(board, position):
    return board[position] == ' '


def play(positions, row1, row2, row3, turn):
    """
    :param positions: List[int]
    :param row1: List[string]
    :param row2: List[string]
    :param row3: List[string]
    :param turn: string
    :return: null

    function to apply userInput to grid
    """
    row, column = positions[0], positions[1] - 1

    if row == 1:
        if not row1[column].isspace():
            print("That space is already filled please try again.")
            return False
        else:
            if turn:
                row1[column] = "X"
            else:
                row1[column] = "O"
    elif row == 2:
        if not row2[column].isspace():
            print("That space is already filled please try again")
        else:
            if turn:
                row2[column] = "X"
            else:
                row2[column] = "O"
    elif row == 3:
        if not row3[column].isspace():
            print("That space is already filled please try again")
        else:
            if turn:
                row3[column] = "X"
            else:
                row3[column] = "O"


def win_check(mark, row1, row2, row3):
    """
    :param mark: string
    :param row1: List[string]
    :param row2: List[string]
    :param row3: List[string]
    :return:
    """
    return ((row1[0] == mark and row1[1] == mark and row1[2] == mark) or  # across the top
            (row2[0] == mark and row2[1] == mark and row2[2] == mark) or  # across the middle
            (row3[0] == mark and row3[1] == mark and row3[2] == mark) or  # across the bottom
            (row1[0] == mark and row2[0] == mark and row3[0] == mark) or  # down the left side
            (row1[1] == mark and row2[1] == mark and row3[2] == mark) or  # down the middle
            (row1[2] == mark and row2[2] == mark and row3[2] == mark) or  # down the right side
            (row1[0] == mark and row2[1] == mark and row3[2] == mark) or  # diagonal (left to right)
            (row1[2] == mark and row2[1] == mark and row3[0] == mark))  # diagonal (right to left)


def full_check(row1, row2, row3):
    """
    :param row1: List[string]
    :param row2: List[string]
    :param row3: List[string]
    :return: bool

    checks if board is full
    """
    return row1.count(" ") == 0 and row2.count(" ") == 0 and row3.count(" ") == 0  # returns true if all spaces in
    # grid are filled


def game():
    row1 = [" ", " ", " "]
    row2 = [" ", " ", " "]
    row3 = [" ", " ", " "]  # used lists as representation of grid for simplicity
    player1 = True
    global player1_score
    global player2_score
    print("Hello there, welcome to my tic tac toe game, I hope you enjoy.")
    print("The rules are simple, get three in a row and you win!!")
    print(f"Current score: X:{player1_score}   O:{player2_score}")
    print("Here is the starting grid:")  # welcome message
    display(row1, row2, row3)
    while True:
        if win_check("X", row1, row2, row3):  # check if grid matches win condition for p1
            print("Player 1 wins!!")
            player1_score += 1
            break
        elif win_check("O", row1, row2, row3):  # check if grid matches win condition for p2
            print("Player 2 wins!!")
            player2_score += 1
            break
        elif full_check(row1, row2, row3):  # checks if board is full
            print("No winner this time unfortunately.")
            break
        user_input = input("Choose a square (row,column): ")
        result = check(user_input)
        if not result:
            print("Invalid input, please try again")
        else:
            play(result, row1, row2, row3, player1)
            display(row1, row2, row3)
            player1 = not player1  # boolean variable to indicate who's go it is

    if input("Would you like to play again? (y/n): ").lower() == "y":
        game()  # if user decides to play again, function is called again


game()
