n=int(input("Enter the number: "))
sum=0
for i in range(3):
    i=int(pow(n,i+1))
    print(i)
    sum=sum+i
print("sum is",sum)