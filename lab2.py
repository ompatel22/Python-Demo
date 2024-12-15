# def fib(n):
#     if n==1 or n==2:
#         return n-1
#     else:
#         return fib(n-1)+fib(n-2)
    
# for i in range (1,11,1):
#     print(fib(i),end=" ")

import numpy as np

arr=np.array([1,2,3,4,5])
sum=0
for i in range(5):
    sum+=arr[i]
print('sum: {}'.format(str(sum)))
print('arr[1]:',arr[1])
print()

print('1D arr slicing')
print(arr,'\n')
print(arr[0],'\n')
print(arr[2:],'\n')
print(arr[:3],'\n')
print(arr[-1],'\n')
print(arr[-3:],'\n')
print(arr[1:2],'\n')

arr1=np.array([[1,2,3],[4,5,6],[7,8,9]])
print('2D arr slicing')
print(arr1,'\n')
print(arr1[0,2],'\n')
print(arr1[2,:],'\n')
print(arr1[1,:],'\n')
print(arr1[1:2,0:1],'\n')
print(arr1[1:3,0:2],'\n')
print(arr1[1:2],'\n')

print('\nQ4')
a=np.array([1,2,3,4,5])
b=np.array([6,7,8,9,10])
print('Add:',a+b)
print('Sub:',a-b)
print('Mul:',a*b)
print('Div:',b//a)

print('\nQ6')
aa=np.array([[1,2,3],[4,5,6],[1,2,3]])
bb=np.array([[4,5],[1,2],[2,3]])
cc=np.array([[7,8,9],[3,4,5],[1,2,3]])
print('cross:\n',np.cross(aa,bb))
print('dot:\n',np.dot(aa,bb))
print('transpose(aa):\n',np.transpose(aa))

import pandas as pd
print('\nPandas:')
l1=pd.DataFrame([[1,2,3],[4,5,6]], columns=['A','B','C'])
print(l1,'\n')

l2=pd.Series([1,2,3],index=['A','B','C'])
print(l2)

df=pd.read_csv("/Users/om/Documents/student_dataset.csv")
print(df)