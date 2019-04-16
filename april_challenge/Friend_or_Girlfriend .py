
'''
All submissions for this problem are available.### Read problem statements in Hindi, Bengali, Mandarin Chinese, Russian, and Vietnamese as well.

Shlok and Sachin are good friends. Shlok wanted to test Sachin, so he wrote down a string S
with length N and one character X. He wants Sachin to find the number of different substrings of S which contain the character X

at least once. Sachin is busy with his girlfriend, so he needs you to find the answer.

Two substrings of S
are considered different if their positions in S are different.
'''
import psyco

psyco.full()

list1 = []
list2 = []
def subString(Str,n): 
      
    # Pick starting point 
    for Len in range(1,n + 1): 
          
        # Pick ending point 
        for i in range(n - Len + 1): 
              
            # Print characters from current 
            # starting point to current ending 
            # point.  
            j = i + Len - 1

            for k in range(i,j + 1): 
                #print(Str[k],end="")
                list1.append(Str[k])
                s=''.join(list1)
                #print(s)
                #list1.append(Str[k])

            list2.append(s)
            s = None
            list1.clear()
            #print() 
              

count = 0
prin = []
test_case = int(input())
for i in range(test_case):
    no_of_index = int(input()) 
    the_string = input()
    Str,aplhabet = the_string.split(" ")
    subString(Str,len(Str)) 
    #for i in len(list1):
    #print(list2)
    
    for i in list2:
        li = list(i)
        for i in li:
            if(i==aplhabet):
                count+=1
                break
    prin.append(count)
    count=0

for i in prin:
    print(i)

