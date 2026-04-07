# wap to print fizual number fizz->3  buzz->5 fizzbuzz->3,5
for i in range(1, 50):
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)
