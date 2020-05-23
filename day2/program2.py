n=int(input("Enter a number="))
a=0
b=1
print("The fibanaci series is:=")
for i in range(n):
	print(a)
	c=a+b
	a=b
	b=c
