# looping Through
print("\n-----LOOPING")

for x in "Banana":
    print(x, end=" ")

# Check String
print()
print("\n-----Check string")

txt = "The best things in life are free"
print("free" in txt)

# If in String
print("\n-----If in string")
txt = "The best things in life are free"
if "free" in txt:
    print("Yes, 'free' is present")

# NOT
print("\n-----NOT")
print("expensive" not in txt)

# In in IF
print("\n----- In in IF")
if "expensive" not in txt:
    print("No, 'expensive' in NOT present")
