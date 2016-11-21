from sympy import *
from math import *

from collections import OrderedDict
from operator import mul 


def main():


	fig = []
	choice = None
	
	while True:
		print(
		"""
		************************************
		*
		*	Меню
		*								   
		*	0-выход						   
		*	1-добафить фигуру			   
		*	2-список фигур				   
		*								   
		*								   
		*								   
		*								   
		************************************
		"""
		)	
	
	
		choice = input('выбрать--->>>	')

		menu_choice = {
			'0': choices_exit,
			'1': draw_choices,
			'2': choices_base

		}

		menu_func = menu_choice.get(choice, None)
		menu_func() if menu_func is not None else None

def choices_exit():
	print('Досвидание, до новых встреч')
	exit()


def choices_base():
	with open('001.txt', 'r') as f:
			for line in f.readlines():
				print(line)
				

	
	

def draw_choices():


	print(
		"""
		************************************
		*								   
		*	0-треугольник				   
		*	1-прямоугольник				   
		*	2-квадрат					   
		*								   
		*								   
		*								   
		*								   
		************************************
		"""
			)
	draw_choices = {
		'0': draw_triangle,
		'1': draw_rectangle,
		'2': draw_square

	}
	choice = input('выбераем фигуру--->>>	')

	draw_func = draw_choices.get(choice, None)
	draw_func() if draw_func is not None else None
		
def draw_triangle():
	print(
	"""     
	     C
	     *
	  
	          
	   	  
	A *      *B
	     

	заполним значений координат "А" "В" "С"
	"""	
		)
	cords = input_cords(['A', 'B', 'C'])
	print(
		'\n'.join(['Координаты {0}: {1}'.format(key, str(cords)) for key, cords in cords.items()])
	)

	sides = {
		'AB': sqrt(((cords['B'][0])-cords['A'][0])**2)+((cords['B'][1]-cords['A'][1])**2),
		'AC': sqrt(((cords['C'][0])-cords['A'][0])**2)+((cords['C'][1]-cords['A'][1])**2),
		'BC': sqrt(((cords['C'][0])-cords['B'][0])**2)+((cords['C'][1]-cords['B'][1])**2)
	}
	

	p = sum(sides.values()) / 2
	area = sqrt((p-sides['AB'])*(p-sides['AC'])*(p-sides['BC'])*p)

	print(
		'\n'.join(['Сторона {0}: {1}'.format(key, str(side)) for key, side in sides.items()])
	)

	print('площадь треугольника равна--->>> ', area,)
	with open('001.txt', 'w+') as f:
		f.write('\n площадь треугольника %s' % area)


def input_cords(keys):
	cords = OrderedDict(keys=keys)
	for cord_name in keys:
		no_parse_cords = input('точка %s: Введите координаты через запятую => ' % cord_name)
		cords[cord_name] = [float(cord.strip()) for cord in no_parse_cords.split(',') if cord.strip()]

	return cords


def draw_rectangle():
	print(
		"""



	   A 	      B
     	*     	   *    


     	*     	   *
	  C    	      D





	заполним значений координат "А" "В" "С" "D"
		"""
			)
	cords = input_cords(['A', 'B', 'C', 'D'])

	print(
		'\n'.join(['Координаты {0}: {1}'.format(key, str(cords)) for key, cords in cords.items()])
	)
	sides = {
		'AB': sqrt(((cords['B'][0])-cords['A'][0])**2)+((cords['B'][1]-cords['A'][1])**2),
		'BC': sqrt(((cords['C'][0])-cords['B'][0])**2)+((cords['C'][1]-cords['B'][1])**2)
	}
	area = (sides['AB'])*(sides['BC'])
	print(
		'\n'.join(['Сторона {0}: {1}'.format(key, str(side)) for key, side in sides.items()])
	)

	print('площадь прямоугольника  равна--->>> ', area,)
	with open('001.txt', 'a+') as f:
		f.write('\n площадь прямоугольника %s' % area)

def draw_square():
	print(
		"""



	   A 	   B
     	*      *    


     	*      *
	  C    	   D





	заполним значений координат "А" "В" "С" "D"
		"""
			)
	cords = input_cords(['A', 'B', 'C', 'D'])

	print(
		'\n'.join(['Координаты {0}: {1}'.format(key, str(cords)) for key, cords in cords.items()])
	)
	sides = {
		'AB': sqrt(((cords['B'][0])-cords['A'][0])**2)+((cords['B'][1]-cords['A'][1])**2)
		
	}
	area = (sides['AB'])**2
	print(
		'\n'.join(['Сторона {0}: {1}'.format(key, str(side)) for key, side in sides.items()])
	)

	print('площадь квадрата  равна--->>> ', area,)
	with open('001.txt', 'a+') as f:
		f.write(' \n площадь квадрата %s' % area)




			 


if __name__ == '__main__':
	main()