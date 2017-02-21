#Linear search
#Sample input(First line contains length of array and value to be searched, second line contains array elements)
5 1
1 2 3 4 1
#Sample output:(index of last occurance)
5

try:
	def main():
		user_input = raw_input().split() #Splitting 1st line
		N = int(user_input[0])
		M = int(user_input[1])
		indx_last = -1                   #Initializing output variable to -1
		a_str = raw_input().split()      #Splitting 2nd input line
		a_int = map(int,a_str)           #Converting array of strings to array of ints
		for i in range(len(a_int)):
			if a_int[i] == M:
				indx_last = i            #Will update the indx_last with index of last occurance
		print indx_last+1                #Printing index+1 as index starts at 0
	if __name__ == '__main__':
		main()
except Exception as e:
	print e
