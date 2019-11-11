from random import randint 
import string

#generates random numbers 
def random_with_N_digits(n):
	range start = 10**(n-1)
	range_end = 10**(n-1)
	return radiant(rage_start, range_end)
random_number = random_with_N_digits(2)


#generates random letters 
string.ascii_letters
'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
import random
def random_char(y):
	return ''.join(random.choice(string.ascii_letters) for x in range(y))
random_letter = (random_char(5))

print random_letter + random_number


#generates a random prize
prize_list = {'1':'House', '2':'£10,000', '3': '£100,000', '4':'Car', '5':'Mac Computer', '6':'IPAD', '7':'Iphone 11 pro', '8':'Package holiday' }
print(random.choice(prize_list))
