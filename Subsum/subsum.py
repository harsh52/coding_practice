#list1 = [[9,14],[2,4],[5,18],[7,1],[4,25],[2,20],[5,8],[7,10],[4,12],[3,5]]
import re
list1=[]
with open("Marks.txt") as file:
	line1=re.split(',|\n',file.read().strip())
print(line1)
for i in range(len(line1)):
	line2=line1[i].split()
	line2[0]=int(line2[0])
	line2[1]=int(line2[1])
	list1.append(line2)

list2 = [0]*10
# Greedy algorith to solve problem
list1.sort(key=lambda x: x[1], reverse = True)
for i in list1:
	for j in i:
		p=j
		while(p!=0):
			if(list2[p]==0): 
				list2[p]=i[1] #Inserting data into a list2
				break
			else:
				p-=1
		break
su = 0
for element in list2: # sum of all the element into a list
	su+=element
print("Optimal sequence:",list2,end='\n')
print("Manimum marks can be obtained is:",su)
