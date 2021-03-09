# Author: Terence Tang
# Class: CS325 Analysis of Algorithms
# Assignment:  Portfolio Project - Sudoku Puzzle Game
# Date: 3/8/2021
# Description:  Program for reading a dataset which contains preset sudoku puzzles.  Returns random puzzles from the
#               dataset as requested.
#               Sudoku data provided from Kaggle - https://www.kaggle.com/bryanpark/sudoku

import csv
import random


class Data:
    """ Data object which represents sudoku puzzle data provided.  Has methods for getting a random puzzle and
    solution from the dataset. """
    def __init__(self):
        self.headers = []
        self.puzzles = []
        self.solutions = []
        self.read_data_csv_file()

    def read_data_csv_file(self):
        """ Opens and reads the data input csv file and moves info to memory for manipulation """
        with open("sudoku_data.csv", 'r', encoding="utf8") as csv_data_file:
            csv_reader = csv.reader(csv_data_file)
            self.headers = next(csv_reader)

            for sudoku_set in csv_reader:
                self.puzzles.append(sudoku_set[0])
                self.solutions.append(sudoku_set[1])

        csv_data_file.close()

    def get_sudoku_set(self):
        """ Returns a random sudoku puzzle from the dataset. """
        num = random.randrange(len(self.puzzles))
        return self.puzzles[num], self.solutions[num]


def main():
    data = Data()
    print(data.headers)
    sudoku = data.get_sudoku_set()
    print(sudoku)


if __name__ == "__main__":  main()
