str=input("enter the string: ")
dict={}
for i in str:
    if i in dict:
        dict[i]+=1

    else:
        dict[i]=1
print(dict)
print("character frequency: ")
for x,y in dict.items():
    print(x,y)



