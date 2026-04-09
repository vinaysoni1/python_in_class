def factorial_evens(num):
    if num % 2 == 0:
        product = 1       
        for i in range(num):
            product = product * (i+1)
        print(product)
factorial_evens(4)        