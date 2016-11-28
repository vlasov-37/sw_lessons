# -*- coding utf-8 -*-
import random

class SquareMatrix(object):
    def __init__(self, size):
        self.size = size

    def create_matrix(self):
        self._matrix = [[random.randint(1,100) for i in range(0,self.size)] for j in range(0,self.size)]
        return self._matrix

    def get_matrix(self):
        print(self._matrix)

    def get_element(self, i, j):
        try:
            print(self._matrix[i][j])
        except:
            return None

    def add_to_element(self, i, j, value):
        self._matrix[i][j] += value

    def get_transposed_matrix(self):
        for i in range (0, self.size):
            for j in range(i, self.size):
                a = self._matrix[i][j]
                self._matrix[i][j] = self._matrix[j][i]
                self._matrix[j][i] = a


    def print_hypno(self):
        pass

    def print_snake(self):
        for j in range(0, self.size):
            if j%2 == 0:
                for i in range(0, self.size):
                    print(self._matrix[i][j], end = ' ')
            else:
                for i in range(self.size-1, -1, -1):
                   print(self._matrix[i][j], end = ' ')

def main():
    MatrixSize = int(input("Введите размерность матрицы: "))
    Matrix = SquareMatrix(MatrixSize)
    Matrix.create_matrix()
    Matrix.get_matrix()
    Matrix.get_transposed_matrix()
    Matrix.get_matrix()
    Matrix.get_element(1,2)
    Matrix.print_snake()

if __name__ == '__main__':
    main()