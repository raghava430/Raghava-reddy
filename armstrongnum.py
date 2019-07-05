f=int(input())
sum=0
e=f
while f>0:
    g=f%10
    sum=sum+g*g*g
    f=f//10
if e==sum:
    print("yes")
else:
    print("no")
