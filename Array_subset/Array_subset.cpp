#include<iostream>
#include<algorithm>
#include<map>
using namespace std;
/*Find whether an array is subset of another array*/
// in O(n) time

int sub_array(int arr1[], int arr2[], int m, int n)
{
	map<int, int> A; //creating a map of array1
	for(int i=0; i<m ; i++)
	{
		A[arr1[i]]++;
	}
	for(int i=0 ; i<n; i++)
{
	//if element of array2 does not find in element of array1 then return to A.end() 
	if(A.find(arr2[i])==A.end())
	{
		return 0;
		break;
	}
	else
	{
		A[arr1[i]]--;
	}
}
	return 1;
}

int main()
{
	int arr1[] = {1,2,3,4,5,6,7,8,9,0};
	int arr2[] = {6,7,8};
	int m,n,value;
	m = sizeof(arr1);
	n = sizeof(arr2);
	value = sub_array(arr1, arr2, m, n);
	if(value==0)
	{
		cout<<"No sub_array is present";
	}
	else
	{
		cout<<"arr2 Subarray of array 1";
	}
}