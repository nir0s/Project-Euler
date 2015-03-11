def check_div(num):
	x = 20
	while not x == 0:
		if not num%x == 0:
			return
		x -=1
	return True


num = 1
while(1):
	hrm = check_div(num)
	if hrm == True:
		break
	num += 1

print num

