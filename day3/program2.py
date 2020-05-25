from itertools import permutations
n=input("Enter the sting=")
l=list(n)
count=0
n=permutations(l)
for i in (n):
    print(i)
    count=count+1
print("Total number of permutations are=",count)
