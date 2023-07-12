# While Loop
print("While")

i = 0
while i < 10:
    print(i, end=", ")
    i += 1
# While with brake
print("\nBrake")

i = 1
while i < 10:
    print(i, end=(", "))
    if i == 3:
        break
    i += 1

# While with continue
print("\nContinue")

i = 0
while i < 10:
    i += 1
    if i == 5:
        continue
    print(i, end=(", "))
# Else statement
print("\n Else")
i = 1
while i < 10:
    print(i, end=(", "))
    i += 1
else:
    print("\ni is no longer than 10")
