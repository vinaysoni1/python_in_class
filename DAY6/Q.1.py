# wap  which will print sum of all the key whose value are the factor of 12
data = {
    10: 2,
    5: 3,
    20: 4,
    7: 5,
    15: 6,
    100: 12,
    9: 8
}

sum_of_keys = 0
for key, value in data.items():
    if 12%value == 0:
        sum_of_keys += key
print("Sum of keys whose values are factors of 12:", {sum_of_keys})