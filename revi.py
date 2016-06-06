def rev(n,r):
	if(n>=1):
		r=r*10
		r=r+(n%10)
		rev(int(n/10),r)
	elif n<1 :
		print(r)
		return 0
a=int(input("Number"))
rev(a,0)
