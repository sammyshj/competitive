Number is sparse or not

Given a number, check whether it is sparse or not. A number is said to be a sparse number if in binary representation of the number no two or more consecutive bits are set.

Input:
The first line of input contains an integer T denoting the number of test cases. The first line of each test case is number 'N'.

Output:
Print '1' if the number is sparse and '0' if the number is not sparse.

Constraints:
1 <=T<= 100
1 <=n<= 100

Example:
Input:
4
72
12
2
3

Output:
1
0
1
0

n = int(raw_input())
while(n>0):
    a = int(raw_input())
    j = a>>1
    if(a & j):
        print '0'
    else:
        print '1'
    n=n-1
