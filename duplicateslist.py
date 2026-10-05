lst=[1,2,3,4,1,5,6,3]
result=[]
for i in lst:
    if i not in result:
      result.append(i)
print("List after removing duplicates is",result)