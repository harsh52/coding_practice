'''
You are given N numbers and Q queries. There is only one query type, you have to print the Kth number when all the remaining numbers are arranged in ascending order. You have to remove that number from list after query.

Input:
First line of input is N and Q.
Second line of input contains N space separated integer.
Next Q line contains Q integer each representing K described in problem statement.

Output:
Print Q lines each representing the Kth number when all remaining numbers are arranged in ascending order.

Constraints:
1 <= N <= 3 * 10^5
1 <= Q <= 5 * 10^4
1 <= each number <= 10^9
k <= current size of list
SAMPLE INPUT

10 5
79 72 46 40 6 79 17 28 84 27 
2
9
2
5
1

SAMPLE OUTPUT

17
84
27
72
6

Time Limit: 1.0 sec(s) for each inp
'''

input1,input2 = input().split(" ")

input1 = int(input1)
input2 = int(input2)


#list1 = [int(x) for x in input().split(" ")] #Alternate way to take input in a list
#taking input in a list
input3 = input()
list1 = input3.split(" ")
list1 = list(map(int,list1))

'''
for i in range(input1): # set up loop to run 5 times
	number = input().split(" ")
	number = int(number) # prompt user for number
	list1.append(number)
'''
list1.sort()

list2 = []
for i in range(input2):
	p = int(input())
	list2.append(list1.pop(p-1))
	list1.sort()

for i in range(input2):
	print(list2[i])
#print(list1)
#print(input1)
#print(input2)