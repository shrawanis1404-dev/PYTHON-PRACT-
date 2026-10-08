#create a list of 10 numbers.print the sum of last 4 elemets of the list .
#find out the difference between maxium and minimummin(lst) element of the list
#insert a item in a list at 6 th position .this number must be one third of number stored at 4 th position 
lst=[34,32,345,53,45]
print(sum(lst[-4:]))
print(max(lst)-min(lst))

str="shrawani"
print(max(str))
print(min(str))

ele=lst[3]//3
print(lst.insert(5,ele))