str=input("enter a string: ")
str=str.split()
dict={}
for word in str:
    if word in dict:
        dict[word]+=1
    else:
        dict[word]=1
print(dict)
print("character frequency")
for x,y in dict.items():
        print(x,y)

