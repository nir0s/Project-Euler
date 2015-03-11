number = 100


def get_sum_of_squares(num):
	sum = x = 0

	while x <= num:
		sum += x*x
		x += 1
	return sum



def get_square_of_sum(num):
	sum = x = 0

	while x <= num:
		sum += x
		x += 1
	
	square = sum*sum
	return square	

sum_of_squares = get_sum_of_squares(number)
square_of_sum = get_square_of_sum(number)

print square_of_sum
print sum_of_squares
print square_of_sum - sum_of_squares