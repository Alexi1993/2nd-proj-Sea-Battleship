import random
from random import randint

PLAYER_BOARD = [[" "] * 8 for i in range(8)]
COMPUTER_BOARD = [[" "] * 8 for i in range(8)]
PLAYER_GUESS_BOARD = [[" "] * 8 for i in range(8)]
COMPUTER_GUESS_BOARD = [[" "] * 8 for i in range(8)]


def print_board(board):
    print("  A B C D E F G H")
    print("  +-+-+-+-+-+-+-+")
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1


letters_to_numbers = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7
}


def get_ship_location():
    while True:
        try:
            row = input("Enter the row of the ship: ")
            if row in '12345678':
                row = int(row) - 1
                break
        except ValueError:
            print('Enter a valid letter between A-H')
    while True:
        try:
            column = input("Enter the column of the ship: ").upper()
            if column in 'ABCDEFGH':
                column = letters_to_numbers[column]
                break
        except KeyError:
            print('Enter a valid letter between A-H')
    return row, column


# computer create 5 ships
def computer_create_ships(board):
    for ship in range(5):
        ship_row, ship_column = randint(0, 7), randint(0, 7)
        while board[ship_row][ship_column] == "X":
            ship_row, ship_column = get_ship_location()
        board[ship_row][ship_column] = "X"


# player creates 5 ships
def player_create_ships(board):
    for ship in range(5):
        print_board(board)
        ship_row, ship_column = get_ship_location()
        while board[ship_row][ship_column] == "X":
            print("Choose another location")
            ship_row, ship_column = get_ship_location()
        board[ship_row][ship_column] = "X"


# check if all ships are hit
def count_hit_ships(board):
    count = 0
    for row in board:
        for column in row:
            if column == "X":
                count += 1
    return count


computer_create_ships(COMPUTER_BOARD)
player_create_ships(PLAYER_BOARD)
while True:
    # player turn
    while True:
        print('Guess a battleship location')
        print_board(PLAYER_GUESS_BOARD)
        row, column = get_ship_location()
        if PLAYER_GUESS_BOARD[row][column] == "-":
            print("You guessed that one already.")
        elif COMPUTER_BOARD[row][column] == "X":
            print("Hit")
            PLAYER_GUESS_BOARD[row][column] = "X"
            break
        else:
            print("MISS!")
            PLAYER_GUESS_BOARD[row][column] = "-"
            break
    if count_hit_ships(PLAYER_GUESS_BOARD) == 5:
        print("You won!")
        break
        # computer turn
    while True:
        row, column = randint(0, 7), randint(0, 7)
        while COMPUTER_GUESS_BOARD[row][column] == "-":
            row, column = randint(0, 7), randint(0, 7)
        if PLAYER_BOARD[row][column] == "X":
            COMPUTER_GUESS_BOARD[row][column] = "X"
            break
        else:
            COMPUTER_GUESS_BOARD[row][column] = '-'
            print_board(COMPUTER_GUESS_BOARD)
            break
    if count_hit_ships(COMPUTER_GUESS_BOARD) == 5:
        print("The computer won.")
        break


class GameBoard:
    def __init__(self, board):
        self.board = board

    def get_letters_to_numbers():
        letters_to_numbers = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7}
        return letters_to_numbers

    def print_board(self):
        print("  A B C D E F G H")
        print("  +-+-+-+-+-+-+-+")
        row_number = 1
        for row in self.board:
            print("%d|%s|" % (row_number, "|".join(row)))
            row_number += 1


class Battleship:
    def __init__(self, board):
        self.board = board

    def create_ships(self):
        for i in range(5):
            self.x_row, self.y_column = random.randint(0, 7), random.randint(0, 7)
            while self.board[self.x_row][self.y_column] == "X":
                self.x_row, self.y_column = random.randint(0, 7), random.randint(0, 7)
            self.board[self.x_row][self.y_column] = "X"
        return self.board

    def get_user_input(self):
        try:
            x_row = input("Enter the row of the ship: ")
            while x_row not in '12345678':
                print('Please select a valid row')
                x_row = input("Enter the row of the ship: ")

            y_column = input("Enter the column letter of the ship: ").upper()
            while y_column not in "ABCDEFGH":
                print('Please select a valid column')
                y_column = input("Enter the column letter of the ship: ").upper()
            return int(x_row) - 1, GameBoard.get_letters_to_numbers()[y_column]
        except ValueError and KeyError:
            print("Not a valid input")
            return self.get_user_input()

    def count_hit_ships(self):
        hit_ships = 0
        for row in self.board:
            for column in row:
                if column == "X":
                    hit_ships += 1
        return hit_ships


def RunGame():
    computer_board = GameBoard([[" "] * 8 for i in range(8)])
    user_guess_board = GameBoard([[" "] * 8 for i in range(8)])
    Battleship.create_ships(computer_board)
    # start 10 turns
    turns = 10
    while turns > 0:
        GameBoard.print_board(user_guess_board)
        # get user input
        user_x_row, user_y_column = Battleship.get_user_input(object)
        # check if duplicate guess
        while user_guess_board.board[user_x_row][user_y_column] == "-" or user_guess_board.board[user_x_row][
            user_y_column] == "X":
            print("You guessed that one already")
            user_x_row, user_y_column = Battleship.get_user_input(object)
        # check for hit or miss
        if computer_board.board[user_x_row][user_y_column] == "X":
            print("You sunk 1 of my battleship!")
            user_guess_board.board[user_x_row][user_y_column] = "X"
        else:
            print("You missed my battleship!")
            user_guess_board.board[user_x_row][user_y_column] = "-"
        # check for win or lose
        if Battleship.count_hit_ships(user_guess_board) == 5:
            print("You hit all 5 battleships!")
            break
        else:
            turns -= 1
            print(f"You have {turns} turns remaining")
            if turns == 0:
                print("Sorry you ran out of turns")
                GameBoard.print_board(user_guess_board)
                break


if __name__ == '__main__':
    RunGame()
