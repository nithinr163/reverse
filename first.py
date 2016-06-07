n=int(input("Enter the number of inputs:"));
arr=[]
p=0
for i in range(0,n):
	v=int(input("\n Enter element:"))
	arr.append(v)
for i in range(0,n):
	for j in range(i+1,n):
		if(arr[i]==arr[j] and p==0):
			    print("\nElement is ",arr[i])
			    p=1;
		
	if(p>0):
		break
if(p==0):
	print("\n No duplicates")
