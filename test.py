# Task 1

a = 3
b = 3.5
name = 'name'
c = True

# Task 2

first = int(input('Input first number: '))
second = int(input('Input second number: '))
print( first == second)
print( first <= second)
print( first >= second)
print( first != second)
print( first + second)
print( first - second)
print( first * second)
print( first ** second)
if second != 0:
	print( first / second)
	print( first // second)
	print( first % second)

# Task 3

if (first + second) == 10:
	print ('Привет')
elif second != 0:
	
	if (first / second) == 0:
		print('деление первого числа на второе равно нулю!')
else:
	print(first - second)

# Task 4

name = input('Введите имя: ')
print('Привет ', name, 'ты в игре!')
number = int(input('Угадай число от 0 до 100: '))
number_x = 18 
if 0 <= number <= 100:
	if number == number_x:
		print( name, 'ты угадал!')
	else:
		print('Вследующий раз повезет :)')
else:
	print('Введено не корректное число.')
	

