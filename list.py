print("-------------------------------------------------")

examplelist = []
examplelist.append(1)
examplelist.append(2)
examplelist.append(3)
print(examplelist[0]) 
print(examplelist[1]) 
print(examplelist[2]) 

# prints using loop
for listItem in examplelist:
    print(listItem)

print("-------------------------------------------------")

anotherList = [1,2,3]
print(anotherList[1])
#the following will throw an exception, array out of bound
#print(anotherList[10])

print("-------------------------------------------------")
#-------------------------------

even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7]
all_numbers = odd_numbers + even_numbers
print(all_numbers)

print("-------------------------------------------------")