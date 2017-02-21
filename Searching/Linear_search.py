#Linear search
#Sample input(First line contains length of array and value to be searched, second line contains array elements)
5 1
1 2 3 4 1
#Sample output:(index of last occurance)
5

user_input = raw_input().split()
N = int(user_input[0])
M = int(user_input[1])
indx_last = -1

a_str = raw_input().split()
a_int = map(int,a_str)

for i in range(len(a_int)):
	if a_int[i] == M:
		indx_last = i
print indx_last+1
