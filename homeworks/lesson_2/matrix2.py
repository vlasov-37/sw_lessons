import math
import random


class SquareMatrix(object):
    def __init__(self, size):
        self.size = size

    def create_matrix(self):
        # Создаем матрицу с использованием random , сохраняем в атрибут self._matrix и возвращаем ее
        self._matrix = [[random.randint(1,100) for j in range(self.size)] for i in range(self.size)]
        return self._matrix

    def get_matrix(self):
        # отдаем матрицу
        return self._matrix

    def print_matrix(self):
        # выводим матрицу
        [print([self._matrix[i][j] for j in range(self.size)], end='\n') for i in range(self.size)]

    def get_element(self,i,j):
        # вернуть self._matrix[i][j]
        # предусмотреть, что i,j могут быть введены больше чем размерность, тогда вернуть None
        if i or j > self.size:
            return None
        else:
            return self._matrix[i][j]

    def add_to_element(self,i,j, value):
        # Добавить self._matrix[i][j] + value
        self._matrix[i][j] += value

    def get_transposed_matrix(self):
        # вернуть транспонированную матрицу
        self._transposed_matrix = [[0 for j in range(self.size)] for i in range(self.size)]
        [[self._transposed_matrix[i][j] = self._matrix[i][j] for j in range(self.size)] for i in range(self.size)]
        return self._transposed_matrix

    def print_hypno(self):
        # Для матрицы
        # [1, 8, 7],
        # [2, 9, 6],
        # [3, 4, 5]
        # Вывести [1,2,3,4,5,6,7,8,9]
        print([self._matrix[i][j] for j in range(self.size) for i in range(self.size)], end=' ')
        print()

    def print_snake(self):
        # [1, 8, 7],
        # [2, 9, 6],
        # [3, 4, 5]
        # Вывести [1, 2, 3, 4, 9, 8, 7, 6, 5]
        print ("[", end='')
        for j in range(self.size):
            for i in range(self.size):
                if j % 2 == 1:
                    print(self._matrix[(self.size-1) - i][j], end=', ')
                elif i == self.size - 1 and j == self.size - 1:
                    print(self._matrix[i][j], end=']')
                else:
                    print(self._matrix[i][j], end=', ')
        print()

        #print([self._matrix[(self.size - 1) - i][j] for j in range(self.size) for i in range(self.size)], end=' ')

    def make_improvization(self):
        # задача на импровизацию, сделайте сами что-нибудь интересное
        pass

class Matrix(object):
    # Написать матрицу, но уже не квадратную, а размерности N x M, акже задавать через конструктор.
    def __init__(self, sizeX, sizeY):
        self.sizeX = sizeX
        self.sizeY = sizeY

    def create_matrix(self):
        # Создаем матрицу с использованием random , сохраняем в атрибут self._matrix и возвращаем ее
        self._matrix = [[random.randint(1,100) for j in range(self.sizeX)] for i in range(self.sizeY)]
        return self._matrix

    def get_matrix(self):
        # отдаем матрицу
        return self._matrix

    def print_matrix(self):
        # выводим матрицу
        [print([self._matrix[i][j] for j in range(self.sizeX)], end='\n') for i in range(self.sizeY)]

print("Матрица:")
matrix = SquareMatrix
matrix.__init__(matrix, 3)
matrix.get_transposed_matrix(matrix)
matrix.create_matrix(matrix)
matrix.print_matrix(matrix)
matrix.print_snake(matrix)
matrix.print_hypno(matrix)
print()

print("Прямоугольная матрица:")
matrix_one = Matrix
matrix_one.__init__(matrix_one, 8, 5)
matrix_one.create_matrix(matrix_one)
matrix_one.print_matrix(matrix_one)