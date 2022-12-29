
n1 = 0
n2 = 0
nums={'0':0,'1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
for i in num1:
    n1 = 10 * n1 + nums[i]
for i in num2:
    n2 = 10 * n2 + nums[i]

result = n1*n2

print(result)