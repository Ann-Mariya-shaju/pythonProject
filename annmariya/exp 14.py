l1=[12,34,-9,25,-97]
l2=[43,-9,-6,25,8]
x=len(l1)
y=len(l2)
s1=sum(l1)
s2=sum(l2)
if(x==y):
    print("list are same length")
else:
    print("different")
if(s1==s2):
    print("sum of two lists are same")
else:
    print("sum is different")
    print("common elements")
for i in l1:
    for j in l2:
        if(i==j):
           print(i)
