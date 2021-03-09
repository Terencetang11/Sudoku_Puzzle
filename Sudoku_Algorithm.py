# Author: Terence Tang
# Class: CS325 Analysis of Algorithms
# Assignment:  Portfolio Project - Sudoku Puzzle Game
# Date: 3/8/2021
# Description:  Algorithms for checking the validity of a sudoku solution / certificate and for deriving a solution for
#               a given instance of sudoku.  Checking the validity of a provided certificate runs in O(n^2) and
#               algorithm for deriving a solution to the sudoku uses bruteforce backtracking.
#
#               Resources used include the following:
#               https://en.wikipedia.org/wiki/Sudoku_solving_algorithms
#               https://arxiv.org/pdf/cs/0507053.pdf
#               https://stackoverflow.com/questions/65159024/why-this-sudoku-solver-return-same-board-without-solving-anything


def check_solution(board):
    """ Method for verifying if a provided solution/certificate is a valid solution for the sudoku puzzle. """
    # initialize data structures for checking rows, columns and segments
    row_check = [[0 for n in range(9)] for m in range(9)]
    column_check = [[0 for n in range(9)] for m in range(9)]
    segment_check = [[0 for n in range(9)] for m in range(9)]

    # scans by row and column
    for row in range(len(board)):
        for col in range(len(board[row])):
            num = board[row][col] - 1
            segment = int(col / 3) + int(row / 3) * 3       # derives which segment current square resides in

            # updates counts for an instance of a number by it's row, column and segment
            if num >= 0:
                row_check[row][num] = row_check[row][num] + 1
                column_check[col][num] = column_check[col][num] + 1
                segment_check[segment][num] = segment_check[segment][num] + 1

            # if the count of any number is greater than 1, it has been repeated; thus returning not solved
            if row_check[row][num] > 1 or column_check[col][num] > 1 or segment_check[segment][num] > 1:
                print(row, col)
                return "Not solved, try again!"

    # if no repeats encountered, returns solved
    return "Solved!"


def solve_sudoku(board):
    """ Wrapper method for calling the recursive backtracking method to solve the sudoku puzzle.  Also copies the
     puzzle board over to retain fidelity of the original puzzle. """
    solution_board = []
    for row in board:
        solution_board.append(row[:])

    solve_sudoku_recursive(solution_board)
    return solution_board   # returns solution


def solve_sudoku_recursive(board):
    """ Bruteforce backtracking algorithm for deriving a solution to a sudoku puzzle.  For each empty square,
    checks if any entry from 1 to 9 is valid, attempts that entry and then recursively checks the next square.
    If solution found to be invalid, back tracks up stack and removes original selection. """
    # for each next empty square
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:

                # for each valid entry
                for input in range(1, 10):
                    if check_valid_move(board, row, col, input):

                        # try entry and recursively call down, if solution found, returns True back up stack
                        board[row][col] = input
                        if solve_sudoku_recursive(board):
                            return True
                        # if solution not valid, undoes current square input to allow backtracking to previous square
                        board[row][col] = 0

                # if no other valid entries available returns false and enables back tracking
                return False
    # if sudoku has been filled out, then return True
    return True


def check_valid_move(board, row, col, input):
    """ Method for determining if a specific input is allowed at a specific square. Returns false if invalid input,
    returns True if valid input. """

    # checks for duplicates in row and column
    for i in range(9):
        if board[row][i] == input or board[i][col] == input:
            return False

    # checks for duplicates in segment (3x3 square)
    seg_x = int(col / 3) * 3
    seg_y = int(row / 3) * 3
    for x in range(3):
        for y in range(3):
            if board[seg_y + y][seg_x + x] == input:
                return False

    # if no dupes encountered, returns True
    return True


def main():
    pass


if __name__ == "__main__":  main()