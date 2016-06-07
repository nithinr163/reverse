n=int(input("Enter the number of inputs:"));
arr=[]
for i in range(0,n):
	v=int(input("Enter element"))
	arr.append(v)
for i in range(0,n):
	if(arr[i]==i):
		print("\nElement is ",arr[i])
