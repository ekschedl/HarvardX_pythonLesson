# ----Dict ----

dict ={
    "name": "Valera",
    "Surname": "Bobkov",
    "age": 19
}
print(dict)
print(dict["age"])
dict["new surname"] = "Schedl"
print(dict)

# --------

name = "Harry"
print(name[0]) # H

# ---- List ----
names = ["Harry", "Marry", "Werry", "Ginny"]
print(names) # ['Harry', 'Marry', 'Werry']
print(names[0]) #Harry

names.append("Draco-append")
print(names) #['Harry', 'Marry', 'Werry', 'Ginny', 'Draco-append']

names.sort()
print(names) #['Draco-append', 'Ginny', 'Harry', 'Marry', 'Werry']


# ---- Set ----
s = set()
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(3) # will not take, elements must be unique
s.remove(2)
print(s)
print(f"The set has {len(s)} elements")
print("---------")


set1 = {3, 5, 5}
set2 = {8, 4, 5}
union_set = set1 | set2  # Объединение
print(union_set)  # Вывод: {3, 4, 5, 8}
print("---------")