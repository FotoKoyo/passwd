import random

def passwd():
	chars = 'qwertyuiopasdfghjklzxcvbnm123456789'


	number = int(input("Сколько паролей --> "))

	lenght = int(input("Сколько чисел --> "))

	for n in range(lenght):
		password = ''
		for i in range(lenght):
			password = password + random.choice(chars)

		print(password)

while True:
	passwd()