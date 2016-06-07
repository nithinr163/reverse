n=int(input("Enter the number of inputs:"));
arr=[]
small=None
for i in range(0,n):
	v=int(input("\n Enter element:"))
	arr.append(v)
sarr=sorted(arr)
small=abs(sarr[0]+sarr[1])
a=sarr[0]
b=sarr[1]
for i in range(0,n):
	for j in range(1,n):
		temp=abs(sarr[i]+sarr[j])
		if(small>temp):
			small=temp
			a=sarr[i]
			b=sarr[j]
print("\n The numbers are ",a,b)
