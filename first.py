n=int(input("Enter the no. of elements:"))
arr=[]
c=0
for i in range(0,n):
    v=int(input("Enter the value:"))
    arr.append(v)
    if(i>0 and c==0):
        for j in range(0,i):
            if(v==arr[j]):
                dup=v
                c=1
if(c==1):
    print("\nDuplicate:",dup)                
else:
    print("\n No duplicate")
