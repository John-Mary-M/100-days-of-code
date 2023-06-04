#!/usr/bin/python3
# More on the random Module. 4/06/2023

import random

def main():
#Generating float numbers between 0 and 1
	randomFloat = random.random()
	print('randomFloat', randomFloat)

#Generating a random integer within a specified range (exclusive of the stop value).
	random_int = random.randrange(0, 10, 1)
	print('random_int:', random_int)

#Generating a list of random elements from a list
	myList = [1, 2, 3, 4, 5]
	rand_Elements = random.choices(myList, k=3)
	print('random Elements:', rand_Elements)
'''
random.choices(sequence, weights=None, cum_weights=None, k=1)
k = 3 determines the length of the returned list
weights default is None. provides ability to weigh the posibility of each value.
cum_weights: provides ability to weigh the posibility of each value but the weights are accumlated. eg. normal weight list [2, 1, 1] cum_weight list [3, 4, 5]
'''

#Initializing the random number generator with a seed value for reproducible results
	#set seed value to 42
random.seed(45)
	#generate random number btn 1 and 10
rand_num = random.randint(1, 10)
print('rand_num:', rand_num)

#Generating random integers with specific number of bits
rand_bits = random.getrandbits(8)
print('rand_bits', rand_bits)


if __name__=="__main__":main()
