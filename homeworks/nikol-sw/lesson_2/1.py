from random import randint

class SquareMatrix(object):
    def __init__(self, size):
        self.size = size

    def create_matrix(self):
        # Создаем матрицу с использованием random , сохраняем в атрибут self._matrix и возвращаем ее
        print('Задайте размерность матрицы:')
        n = int(input()) #размерность массива
        self._matrix = [[randint(-5, 5) for j in range(n)] for i in range(n)]
        return self._matrix

    def get_matrix(self):
    # отдаем матрицу
        self.create_matrix()
        print(self._matrix)
        return self._matrix
        

    def get_element(self,i,j):
        # вернуть self._matrix[i][j]
        # предусмотреть, что i,j могут быть введены больше чем размерность, тогда вернуть None
        return self._matrix[i][j]
        if (i>n)or(j>n):
            return None
        

    def add_to_element(self,i,j, value):
    # Добавить self._matrix[i][j] + value
        print('Введите элемент, к которому нужно добавить значение:')
        i=int(input())
        j=int(input())
        print('Введите значение, которое нужно добавить:')
        value=int(input())
        self.get_element()
        if (self._matrix[i]==i)and(self._matrix[j]==j):
            self._matrix[i][j]+=value
       

    def get_transposed_matrix(self):
        # вернуть транспонированную матрицу
        t=0
        self.get_matrix()
        for i in range(n):
            for j in range(n):
                self._matrix[i] = self._matrix[j]

        return self._matrix

    
    def print_hypno(self):
        # Для матрицы
        # [1, 8, 7],
        # [2, 9, 6],
        # [3, 4, 5]
        # Вывести [1,2,3,4,5,6,7,8,9]
        m = 3
        n = 3
        matr = np.array([1, 8, 7], [2, 9, 6], [3, 4, 5])
        for j in range(m):
           for i in range(n):
               if (matr[i][j]<matr[i][j+1]):
                   print(matr[i][j])
        

    def print_snake(self):
        # [1, 8, 7],
        # [2, 9, 6],
        # [3, 4, 5]
        # Вывести [1, 2, 3, 4, 9, 8, 7, 6, 5]
        pass

    def make_improvization(self):
        # задача на импровизацию, сделайте сами что-нибудь интересное
        pass

class Matrix(object):


    def create_matrix():
        # Написать матрицу, но уже не квадратную, а размерности N x M, также задавать через конструктор.
        print('Задайте количество строк:')
        n = int(input()) #количество строк
        print('Задайте количество столбцов:')
        m = int(input()) #количество столбцов
        matrix = [[randint(-5, 5) for j in range(m)] for i in range(n)]
        print(matrix)


SquareMatrix(2).get_matrix()

	
	
        pass

    def print_snake(self):
        # [1, 8, 7],
        # [2, 9, 6],
        # [3, 4, 5]
        # Вывести [1, 2, 3, 4, 9, 8, 7, 6, 5]
        pass

    def make_improvization(self):
        # задача на импровизацию, сделайте сами что-нибудь интересное
        pass

class Matrix(object):
    # Написать матрицу, но уже не квадратную, а размерности N x M, также задавать через конструктор.
	print('Задайте количество строк:')
	n = int(input()) #количество строк
	print('Задайте количество столбцов:')
	m = int(input()) #количество столбцов
	matrix = [[randint(-5, 5) for j in range(m)] for i in range(n)]
	
    
