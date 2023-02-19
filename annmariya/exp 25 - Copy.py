n=int(input("first number: "))
m=int(input("second number: "))
gcd=1
for i in range(1,max(n,m)):
    if n%i==0 and m%i==0:
        gcd=i
print("gcd of 2 numbers:",gcd)