n=int(input("Enter the number of inputs:"));
arr=[]
for i in range(0,n):
	v=int(input("\n Enter element:"))
	arr.append(v)
sarr=sorted(arr)
for i in range(0,n):
	p=0
	for j in range(i+1,n):
		if(sarr[i]==sarr[j]):
			p=p+1
	k=sarr[i]	
	i=i+p
	i=i+1
	if(p==0):
		print(k,"is unique")
	if(i>=n):
		break
		
    
