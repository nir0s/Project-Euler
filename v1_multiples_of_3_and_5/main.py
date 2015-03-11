from collections import Counter

sum = 0
runner = 1
limit = 1000
multipliers = [3,5]
result_list = []

while runner < limit:
    #print 'runner=%s' % runner
    for multiplier in multipliers:
        if multiplier*runner < limit:
            i = multiplier*runner
            result_list.append(i)
            #print 'result=%s' % i
    runner += 1

result_list = Counter(result_list)
for x in result_list:
    print x
    sum += x


print sum
