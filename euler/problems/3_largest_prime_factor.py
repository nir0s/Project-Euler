number = 600851475143
#number = 1092
x = number

def is_prime(x):
	y = x - 1
	while not y == 1:
		print y
		if x%y == 0:
			return False
		else:
			y -= 1
	return True
	
'''
if is_prime(x):
	print '%s is prime' % x
else:
	print '%s is not prime' % x
'''

while not x == 1:
	if is_prime(x):
		if number%x == 0:
			print '%s' % x
			result = x
			break
	x -= 1

print result