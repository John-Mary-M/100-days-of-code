#!/usr/bin/python3
# learning more about the random module
#3/06/2023

import random

def main():
#module can be used to generate a random int between a specified range (inclusive of the last digit in the range)
	random_num = random.randint(1, 10)
	print('random_number:', random_num)

#Generate random floating point between two specified values
	rand_float = random.uniform(0, 1)
	print('rand_float:', rand_float)

#Select a random element from a sequence eg list or tuple
	myList = [1, 2, 3, 4, 5]
	rand_choice = random.choice(myList)
	print('Entire list from which a choice is to be made', myList)
	print('rand_choice', rand_choice)

#Shuffling a list in place with random.shuffle
	random.shuffle(myList)	#doesnt not return new list. 
				#just shuffles the current list
	print('Shuffled list/ newList:', myList)

#Generating random sample of of data
	randomSample = random.sample(myList, 3)
	print('random sample of 3 elements from myList:', randomSample)

if __name__ == "__main__":main()
