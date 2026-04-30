# st=set()
# st1={10,20,30, "vinay"}
# print(st1)
# print(type(st))
# print(type(st1))
# st1.add(100)
# print(st1)

# for i in st1:
#     print(i,end=" ")


set1={10,20,30} # set is unorderd and unindexed and mutable but it can not contain duplicate values and it can not contain list because list is mutable
print(set1)
set1.remove(20)
print(set1)

thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
thisset.clear()

print(thisset)
thisset.add("orange")
thisset.add("grape")
thisset.add("melon")
print(thisset)

thisset.update(["kiwi", "mango", "papaya"])
print(thisset)