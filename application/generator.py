#!/usr/bin/python
# -*- coding: UTF-8 -*-
from random import randint 
import string

#generates random numbers 
def random_with_N_digits(n):
	range_start=10**(n-1)
	range_end=10**(n-1)
	return randint(range_start, range_end)
random_number = str(random_with_N_digits(2))


#generates random letters 
string.ascii_letters
'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
import random
def random_char(y):
	return ''.join(random.choice(string.ascii_letters) for x in range(y))
random_letter = str(random_char(5))



#generates a random prize
prize_list = ['House', '£10,000', '£100,000', 'Car', 'Mac Computer', 'IPAD', 'Iphone 11 pro', 'Package holiday' ]
print(random.choice(prize_list))
