f=open('travels.txt','r')
a=0
b=0
c=0
lipki=0
s=0
d={}
for i in f:
    l=i.split()
    if int(l[0])==1:
        a+=int(l[6])
    if int(l[0])==2:
        b+=int(l[6])
    if int(l[0])==3:
        c+=int(l[6])
    if str(l[2])=='Липки':
        lipki+=int(l[6])
    if int(l[0])==1:
        s+=int(l[4])
    d[str(l[2])]=0

print(d)
l2=[a,b,c]
print(max(l2))
print(lipki)
print(s)
