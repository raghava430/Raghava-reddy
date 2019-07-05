c,e=map(int,input().split())
for k in range(c+1,e):
    s=0
    temp=k
    while(temp>0):
        a=temp%10
        s+=a**3
        temp//=10
    if(k==s):
        print(k,end=" ")
