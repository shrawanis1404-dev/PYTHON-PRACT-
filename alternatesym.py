n=int(input("Enter number of rows"))
for i in range(1,n+1):
    spaces=" "*(n-i)
    if i%2==1:
        sym="@"
    else:
        sym="$"
print(spaces+(sym+" ")*i)