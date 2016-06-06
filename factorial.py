def fact(i):
	if(i==1):
		return i
	else:
		return i*fact(i-1)
n=int(input("Enter the number:"))
fac=fact(n)
print("\nFactorial:",fac)
