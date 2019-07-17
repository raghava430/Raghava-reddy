N=int(input())
li=list(map(int,input().split()[:N]))
l=[]
for i in li:
    if li.count(i)>1:
        if i n ot in l:
            l.append(i)
            print(i,end=" ")
if len(1)==0:
    print('unique')
