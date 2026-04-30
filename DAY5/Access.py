car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x=car.keys()
x=car.values()  
print(x)

car["color"]="red"
car["year"]=2020
print(car)

# Update Dictionary
car.update({"year":2000})
car.update({"color":"blue"})
car.update({"price":50000})
print(car)


#  Remove Dictionary Items
# car.pop("model")
# car.popitem()
del car["model"]
print(car)

# Copy Dictionary
mycar=car.copy()
print(mycar)