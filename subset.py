n=int(input("Enter the no. of elements:"))
arr=[]
sub=[]
for i in range(0,n):
    v=int(input("Enter the value:"))
    arr.append(v)
m=int(input("Size of subste:"))
for i in range(0,m):
    v=int(input("Enter the value:"))
    sub.append(v)
for i in range(0,m):
    f=1
    for j in range(0,n):
        if(sub[i]==arr[j]):
            f=0
    if(f==1):
        break
if(f==0):
    print("\n Subset")
else:
    print("\n Not a subset")
