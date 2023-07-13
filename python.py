# For loops
print("\n-----For loop\n")

b = "banana"
fruits = ["apple", b, "cherry"]
for x in fruits:
    print(x, end=", ")

# looping through
print("\n\n----- Looping through\n")
for x in b:
    print(x, end=", ")

# Break
print("\n\n-----Break\n")
for x in fruits:
    print(x)
    if x == "banana":
        break
for x in fruits:
    if x == "banana":
        break
    print(x)


# Range Function
print("\n-----Range\n")

for x in range(6):
    print(x, end=",")

print("\nrange 2-6")
for x in range(2, 6):
    print(x, end=",")
print("\n\nrange 2-4, step 4")
for x in range(2, 30, 4):
    print(x, end=",")

print("\n\n----- else in for")
for x in range(6):
    print(x, end=" ")
else:
    print("\nFinally")

# Nested Loops
print("\n-----Nested Loops\n")

adj = ["red", "big", "tasty"]

for x in adj:
    for y in fruits:
        print(x, y)

# pass
for x in [0, 1, 2]:
    pass

# Great works!
