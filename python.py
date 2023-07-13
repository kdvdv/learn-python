# string format
print("\n----- Format")
age = 34
txt = "My name in John, and I am {}"
print("\n" + txt.format(age))

quantity = 3
item = 234
price = 45.56
myorder = "I want {} pieces of item {} for {} dollars."
myorder = "I want {1} pieces of item {0} for {2} dollars."
print(myorder.format(quantity, item, price))
print(myorder.format(price, item, quantity))
