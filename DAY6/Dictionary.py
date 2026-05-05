tpl = {1:23, 45:2, "hello":5.6, "hii":55, 1:45, 1:65}
print(list(tpl))

# print keys, values and items of a dictionary
print(tpl.keys())
print(tpl.values())
print(tpl.items())

x=3,4,5
print(x)

a,b,c,d=(1,2,3,4)
print(a)
print(b)
print(c)
print(d)

tpl = {1:23, 45:2, "hello":5.6, "hii":55, 1:45, 1:65}
for k,v in tpl.items():
    print(k,v)

# print value of a key using get method
tpl = {1:23, 45:2, 12:5.6, 23:55, 1:45, 1:65}    
print(tpl.get(12))

# delete a key from dictionary
del tpl[45]
print(tpl.pop(12))
print(tpl)

# delete last item from dictionary
tpl = {1:23, 45:2, 12:5.6, 23:55, 1:45, 1:65}    
tpl.popitem()
print(tpl)

# update a dictionary
tpl = {1:23, 45:2, 12:5.6, 23:55, 1:45, 1:65}
tpl.update({45:100, 56:200})
print(tpl)

# fromkeys method
subject = {}.fromkeys(["maths", "english", "hindi"], 0)
print(subject)


# mutable data types
sqr ={2:4, 3:9, 4:16, 5:25}
s=sqr.copy()  # shallow copy
s[2]=5
print(s)
print(sqr)