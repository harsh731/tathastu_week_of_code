def oddeven(n):
    if n%2==0:
        print("NUMBER is an EVEN number=",n)
    else:
        print("NUMBER is an ODD number=",n)

def prime(n):
    if n>0:
        for i in range(2,n):
            if n%i==0:
                print("Number is NOT a PRIME NUMBER=",n)
                break
        else:
            print("Number is a PRIME NUMBER=",n)
    else:
        print("Enter positive number=")
def palindrome(n):
    x=str(n)
    y=str(n)[::-1]
    if x==y:
        print("Number is a palindrome number=",n)
    else:
        print("Number is not a palindrome number=",n)

def armstrong(n):
    sum=0
    temp=n
    while temp>0:
        digit=temp%10
        sum+=digit**3
        temp=temp//10
    if sum==n:
        print("Number is ARMSTRONG number=",n)
    else:
        print("Number is NOT an ARMSTRONG number=",n)

num=int(input("Enter the number which you want to check="))
oddeven(num)
prime(num)
palindrome(num)
armstrong(num)
