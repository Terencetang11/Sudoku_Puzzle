# Author: Terence Tang
# Class: CS325 Analysis of Algorithms
# Assignment:  Portfolio Project - Sudoku Puzzle Game
# Date: 3/8/2021
# Description:  Program for running a sudoku game through command line interface.  Contains a class for the Sudoku
#               puzzle game which will generate a random game from a given sudoku dataset, derive a solution given a
#               backtracking algorithm, and allow players to attempt to solve the puzzle and checks their input /
#               solution through a verification algorithm.


import Sudoku_Data_Reader
import Sudoku_Algorithm as alg


class Sudoku:
    def __init__(self):
        self.board = []
        self.puzzle = []
        self.alg_solution = []
        self.data_solution = []
        self.game_state = "Not Solved, Keep Trying!"
        self.data = Sudoku_Data_Reader.Data()
        self.build_game_board()

    def build_game_board(self):
        """ Builds game board by retrieving a sudoku puzzle preset from a sudoku dataset and then sets up the
        game board.  Also calls a backtracking algorithm to derive a solution for the sudoku puzzle.  """
        # retrieves new sudoku puzzle from dataset
        sudoku_set = self.data.get_sudoku_set()
        sudoku_problem, sudoku_solution = sudoku_set[0], sudoku_set[1]

        # removes old game boards
        self.board = []
        self.puzzle = []
        self.alg_solution = []
        self.data_solution = []

        # sets up sudoku puzzle to array format
        segment = []
        for num in sudoku_problem:
            segment.append(int(num))
            if len(segment) == 9:
                self.board.append(segment)
                self.puzzle.append(segment[:])
                segment = []

        self.alg_solution = alg.solve_sudoku(self.puzzle)   # uses sudoku backtracking algorithm to solve puzzle

        # sets up the provided sudoku puzzle solution from dataset to array format
        for num in sudoku_solution:
            segment.append(int(num))
            if len(segment) == 9:
                self.data_solution.append(segment)
                segment = []

        self.game_state = "Not Solved, Keep Trying!"

    def request_number_input(self):
        """ Requests user input for the row column and number input they would like to enter as the next entry to
         the Sudoku puzzle.  Has some lightweight data validation through a try / except format and asks for another
         input attempt if invalid inputs were provided.  """
        try:
            self.print_board(self.board)
            row = int(input("Please enter row to add number to (0-8): "))
            col = int(input("Please enter column to add number to (0-8): "))
            num = int(input("Please enter number you wish to add (1-9): "))
            response = self.set_number(col, row, num)
            print(response)     # verifies if move was valid or if invalid inputs were provided.
        except:
            print("Invalid input, try again!")
            self.request_number_input()

    def set_number(self, col, row, num):
        """ Checks that inputs are valid and returns informative messages if not.  If input is valid, updates the
         game board and returns an updated game state. """
        if col > 8 or row > 8 or num > 9 or num < 0:
            return "Invalid input, try again!"
        elif self.new_input_does_not_overlap_original_board(col, row):
            if num == 0:
                self.board[row][col] = 0
            else:
                self.board[row][col] = num
            return self.update_game_state()
            # return alg.check_solution(self.board)
        else:
            return "Cannot change this number, try again!"

    def new_input_does_not_overlap_original_board(self, col, row):
        """ Checks if the requested square to change is an original input for the puzzle, which cannot be changed. """
        return self.puzzle[row][col] == 0

    def update_game_state(self):
        """ Checks to see if the sudoku puzzle has been filed out and if it has, checks if solution is valid. """
        # if board is not filled out, returns a valid move message
        for row in self.board:
            if 0 in row:
                return "Valid input"

        # if board is filled out, verifies if solution is valid and updates game state
        self.game_state = alg.check_solution(self.board)
        return self.game_state

    def get_game_state(self):
        """ Method for retrieving game state. """
        return self.game_state

    def get_game_board(self):
        """ Method for retrieving current puzzle board. """
        return self.board

    def print_board(self, board):
        """ Method for printing a puzzle board, given a board input. Adds separators for readability. """
        print("Sudoku Board:")
        count = 0
        for row in board:
            string = ""
            for num in range(len(row)):
                if row[num] != 0:
                    string += str(row[num])
                else:
                    string += "_"
                if num != len(row) - 1:
                    string += "  "
                if (num+1) % 3 == 0 and num != len(row) - 1:
                    string += "|  "
            print(string)
            count += 1
            if count % 3 == 0 and count < 9:
                print("_______________________________")


def play_sudoku(puzzle):
    """ Nethod for playing a game of sudoku.  Prints out rules and instructions and asks for user inputs.  If
    current puzzle is solved, asks player if they would like to play again and provides a new puzzle. """
    print_instructions()

    print("For review and grading purposes purposes, here is a sample solution:")
    puzzle.print_board(puzzle.alg_solution)

    # while puzzle is not solved, continues to ask user for their next input
    while puzzle.get_game_state() != "Solved!":
        puzzle.request_number_input()
    puzzle.print_board(puzzle.get_game_board())

    # if puzzle is solved, asks user if they would like to play again
    play_again = input("Would you like to play again? Y/N: ")
    play_again = play_again.lower()
    if play_again == 'y':
        puzzle.build_game_board()
        play_sudoku(puzzle)
    else:
        print("Thanks for playing!")


def print_instructions():
    """ Prints to console a set of instructions for how to play a game of Sudoku. """
    print("Welcome to the game of Sudoku!")
    print("--------------------------------")
    print("The goal of the game is to fill every 'square' here with a number.")
    print("The rules of the game are simple:")
    print("  Rule No 1: You can only enter numbers 1-9 in each square.")
    print("  Rule No 2: You cannot repeat the use of a number within a row, column or 3x3 segment.")
    print("--------------------------------")
    print("Instructions:")
    print("  - You will be prompted to enter a row, a column, and then a number input.")
    print("  - The rows and column inputs are 0-indexed, meaning it goes from 0-8.")
    print("  - The number input is expected to be 1-9.  Any other inputs will not be accepted.")
    print("  - Once you've filled out every square, the game will automatically check to see if your solution is valid!")
    print("  - If not, it will prompt you to try again, and you can continue to change your inputs or even write")
    print("    over your original entries.")
    print("Good luck, have fun!")


def main():
    puzzle = Sudoku()
    play_sudoku(puzzle)


if __name__ == "__main__":  main()