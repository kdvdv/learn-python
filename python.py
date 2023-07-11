a = 33
b = 33
if b > a:
    print("\n b is greater then a")


print()

if b > a:
    print(" \n b is greater then a")
elif a == b:
    print(" a and b equal")

# else
a = 200
b = 33
if b > a:
    print(" \n b is greater then a")
elif a == b:
    print(" a and b equal")
else:
    print("\n a is greater than b")

print("A") if a > b else print("B")

# else in if multiple statements
print()

a = 3301
b = 330
print("A > B") if a > b else print(str(a), " = ", str(b)) if a == b else print("B")

print()
# And, Or, Not,

a = 200
b = 33
c = 600
if a > b and c > a:
    print("Both conditions are True")

print()
a = 200
b = 33
c = 600
if a > b or c > a:
    print("At least one of the conditions is True")

print()
a = 200
b = 33
c = 600
if not a > b:
    print("A is NOT greater than B")
else:
    print("b is NOT greater than a")

# Nested IF
print()

x = 5
if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print(" but not above 20.")
else:
    print("Above 10!")
