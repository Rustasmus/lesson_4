#name = input('Input name: ').capitlize()
#if name.startswith('A'):
	#print('Hi', name)
#else:
	#print('Пока', name)

#name2 = input('Введи имя: ')
#if name2[0] == 'A' or name2[0] == 'a':
	#print("Привет", name)
#else:
	#print('Пока', name)

# Использем 1 метод и 1 срез

srt_ = "Python"

if srt_.startswith('P'):
	print (srt_[::2])