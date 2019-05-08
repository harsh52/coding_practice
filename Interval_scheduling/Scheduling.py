
'''
1) Sort the activities according to their finishing time
2) Select the first activity from the sorted array and print it.
3) Do following for remaining activities in the sorted array.
…….a) If the start time of this activity is greater than or equal to the finish time of previously selected activity then select this activity and print it.
Time complexity O(nlogn+n^2)
'''
def schedule(arr):
	arr.sort(key= lambda x:x[1])
	print(arr)
	for i in range(len(arr)):
		for j in range(i):
			if(i==len(arr)-2):
				break
			if(i==1 and j==0):
				print("JOB:",arr[j])
			if(arr[i-1][j+1]<=arr[i][j]): #if(end<=start)
				print("-----")
				print("JOB: ",arr[i])
				break
			else:
				arr.remove(arr[i])

				break

arr = [[5,9],[5,7],[8,9],[0,6],[3,4],[1,2]]
if __name__ == '__main__':

 	schedule(arr)