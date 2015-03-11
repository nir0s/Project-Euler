
'''
while not x == 0:
	while not runner == 0:
		res *= x
		runner -= 1
	sum += res
	print sum
	x -= 1
	runner = x
	res = x
'''


def get_power(x):
	runner = res = x
	while not runner == 1:
		res *= x
		runner -= 1
	return res

runner = res = x = 10
sum = 0

while not x == 1:
	res = get_power(x)
	print res
	sum += res
	x -= 1
print sum + 1