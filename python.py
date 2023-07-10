thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "colours": ["red", "white", "blue"],
}
print(thisdict["year"])
print(len(thisdict))
print(type(thisdict))

thisdictt = dict(name="John", age=36, country="Norway")

print(thisdict["colours"])
print(thisdictt)
print(thisdictt["age"])

x = thisdict["brand"]
y = thisdict.get("year")

print(x, y, "DDDDDDDDDD")


k = thisdict.keys()
print(k)
thisdict["color"] = "pink"
print(thisdict)

x = thisdict.values()
print(x)
print("ddddd", thisdict)
# Смена значения в значении ключа
thisdict["year"] = 1985
print(thisdict)
# Возвращение каждого элемента в виде кортежа
print(thisdict.items())

# Проверка наличия ключа в словаре
if "year" in thisdict:
    print("Yes")
