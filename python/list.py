mylist = [10, 20,30,40,50,60,70,80]
print(mylist)
print(type(mylist))
print("Total number of elements :",len(mylist))
print(mylist[0])
print(mylist[-4])

# access by index
for i in range(0,len(mylist)):
    print(mylist[i],end=",")
print()
# direct access
for i in mylist:
    print(i,end=",")