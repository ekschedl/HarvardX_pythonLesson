people =[
    { "name": "Felix", "city": "Graz"},
    {"name": "Cho", "city": "Berlin"},
    {"name": "Elen", "city": "Venice"}
]

# def f(person):
#     return person["name"]
# people.sort(key=f)

# oder
people.sort(key= lambda person: person["name"]) # "lambda" — это ключевое слово для создания коротких, однострочных функций без необходимости явно их именовать.

print(people)