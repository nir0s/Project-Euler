x = 999


def reverse_num(x):

	str_x = str(x)
	str_list = list(str_x)
	rev_list = reversed(str_list)
	rev_num = "".join(rev_list)
	return rev_num


def is_palindrome(x, length):

	disassemble_point = length / 2
	x_str = str(x)
	#print x_str
	part_1 = x_str[0:disassemble_point]
	part_2 = reverse_num(x_str[disassemble_point:])
	if part_1 == part_2:
		pal_list.append(x_str)


def run_nums(x):

	y = x

	while not x == 100:
		while not y == 100:
			res = y * x
			#print 'res:%s' % res
			length = len(str(res))
			if length % 2 == 0:
				is_palindrome(res, length)
			y -= 1
		y = x
		x -= 1

pal_list = []
run_nums(x)
print max(pal_list)
