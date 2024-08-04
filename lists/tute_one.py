thislist = ["apple", "banana", "cherry", "papaw", "pineapple"]
sublist = thislist[-2:]

print(thislist)
print("sublist :", sublist)

# slice lists
print("second item :", thislist[1])
print("first three values :", thislist[0:3]) # end -> index_value + 1
print("first three values v2 :", thislist[:3])
print("all the items :", thislist[:])
print("last three items :", thislist[2:5])
print("items starting from item 3 :", thislist[2:])
print("2nd item to the last :", thislist[1:-1])

# skip
print('skip as 1', thislist[0:5:1])
print('skip as 2', thislist[0:5:2])

# accessing values
print("last value :", thislist[-1])
print("value just before the last value :", thislist[-2])

# [start:end:skip]

print("length of the list :", len(thislist))

if "apple" in thislist:
    print("apple is there in the list")


# changing the items
thislist[-1] = "starberries"
print("items after mutating:", thislist)

thislist[1:3] = ["cherry", "banana"]

# ["apple", "cherry", "banana" ....]
print("swapped :", thislist)

index_value = thislist.index("cherry")
print("index value of item cherry :", index_value)
# removed_value = thislist.pop(index_value)
# print("removed value :", removed_value)
# print(thislist)

index_value = 0
range_of_values = range(0, 9)
print("range of value :", range_of_values)

for i in range(0, len(thislist)):
    print("index :", i)
    print("value :", thislist[i])
    if thislist[i] == "papaw":
        index_value = i

print("index value of papaw :", index_value)


for item in thislist:
    print(item)

