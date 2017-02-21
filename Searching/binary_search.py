#Binary search
#Input Format:
The first line consists of a single integer N denoting the size of array A.The next line contains N unique integers, 
denoting the content of array A. The next line contains a single integer q denoting the number of queries. Each of the next 
q lines contains a single integer x denoting the element whose rank based position needs to be printed.
#Sample input
5
1 2 3 4 5
5
1
2
3
4
5
#Sample output
Output format: You need to print q integers denoting the answer to each query.
1
2
3
4
5

#Program

try:
	def bin_search(low,high,val):
		while low<=high:
			mid = (low+high)/2
			if a_int[mid] == val:
				return mid
			elif a_int[mid] < val:
				low = mid + 1
			else:
				high = mid - 1
		return -1

	def main():
		global a_int
		N = int(raw_input())
		a_str = raw_input().split()
		if len(a_str) == N:
			a_int = map(int,a_str)
		else: 
			print "Invalid input"
			sys.exit()
		q = int(raw_input())
		for i in range(q):
			low = 0
			high = len(a_int)
			val = int(raw_input())
			pos = bin_search(low,high,val)
			print pos+1
	
	if __name__ == '__main__':
		main()
except Exception as e:
	print e
