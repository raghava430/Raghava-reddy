vr,my=map(str,input().split())
if(len(vr)!=len(my)):
    print("no")
else:
    s1=[vr.count(i) for i in vr]
    s2=[my.count(i) for i in my]
if(s1==s2):
    print("yes")
else:
    print("no")
