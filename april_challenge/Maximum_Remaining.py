'''Chef and Dhyey have become friends recently. Chef wants to test Dhyey's intelligence by giving him a puzzle to solve.

The puzzle contains an integer sequence A1,A2,…,AN
. The answer to the puzzle is the maximum of Ai%Aj, taken over all valid i, j

.

Help Dhyey solve this puzzle.'''

size = int(input())
list1 = []*size
list1 = [int(x) for x in input().split(" ")]   
list1.sort()
ma = list1[size-2] % list1[size-1]
print(ma,end="") 