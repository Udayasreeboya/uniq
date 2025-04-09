#program to separate odd & even elements from list 

num_list=[1,2,3,4,5,6,7,8,9,0]
num_odd=[]
num_even=[]
for i in num_list:
    if i%2==0:
        num_even.append(i)
    else:
        num_odd.append(i)
print(num_even+num_odd)


#program to separate unique elements from list and add "*" at EOL
list=[1,2,3,2,3,3,5,7,9]
result=[]
for i in list:
    if i not in result:
        result.append(i)
    elif i in result:
        result.append("*")
print(result)

#program to separate unique elements from list and add "*" at EOL

list=[1,2,3,2,3,3,5,7,9]
result=[]
duplicant_count=0
for i in list:
    if i not in result:
        result.append(i)
    else:
        duplicant_count+=1
result.extend(["*"]*duplicant_count)
print(result)