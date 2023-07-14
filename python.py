def myFunction():
    print("Hello from function")


myFunction()


def myfunction(fname):
    print(fname + " Refsnes")


myfunction("Emil")
myfunction("Tobias")
myfunction("Linus")

# 2 argument in function


def twoargument(fname, Lname):
    print(fname + " " + Lname)


twoargument("Emil", "dkfjkd")


# Arbitrary arguments
def arguments(*kids):
    print("The youngest child is " + kids[0])


arguments("Emil", "Tobias", "Linus")

# Key value syntax


def syntax(child1, child2, child3):
    print("The youngest chils is " + child3)


syntax(child1="Emil", child2="Tobias", child3="Linus")

# Arbitraray keyword Argument


def kwargs(**kid):
    print("His last name is " + kid["lname"])


kwargs(fname="Tobias", lname="Refsnes")

# Default Parameter value


def mycountry(country="Norwey"):
    print("I am from " + country)


mycountry("Sweden")
mycountry()
mycountry("India")
mycountry("Brazil")


# Passing a List as an Argument
def foodmy(food):
    for x in food:
        print(x)


fruits = ["apple", "banana", "cherry"]
foodmy(fruits)


# Return Values
def multip(x):
    return 5 * x + 2


print(multip(3))
print(multip(5))
print(multip(7))


# Pass
def myfunc():
    pass


# Recursion
def tri_recursion(k):
    if k > 0:
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result


print("\n\nRecursion Example Results")
tri_recursion(4)
