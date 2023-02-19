n=input("enter a string: ")
a=n[0]
for i in n:
    if(i==a):
        n=n.replace(a,"$")
        n=a+n[1:]
print(n)