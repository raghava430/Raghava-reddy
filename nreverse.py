r=int(input())
s=0
t=0
while(r!=0):
    t=r%10
    s=(s*10)+t
    r=int(r/10)
print(s)
