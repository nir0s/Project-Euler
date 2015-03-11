limit = 4000000
result = 0

first = 0
second = 1

sum = 0

while result < limit - second:
	result = first + second
	second = first
	first = result
	print result

	if result%2 == 0:
		sum += result

print 'sum=%s' % sum

