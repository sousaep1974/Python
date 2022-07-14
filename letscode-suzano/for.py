cities_names = ["São Paulo", "Londres", "Tóquio", "París"]
for nome in cities_names:
    print(nome)

cities_names = "São Paulo", "Londres", "Tóquio", "París"
for nome in cities_names:
    print(nome)
    
city = {
    "name": "São Paulo",
    "state": "São Paulo",
    "population_millions" : 12.2}
for chave in city:
    print(f"{chave}: {city[chave]}")
    
cities_names = ["São Paulo", "Londres", "Tóquio", "París", "Rio de Janeiro"]
for nome in cities_names:
    nome = 'DJOIASJF'
print(cities_names)


for position in range(len(cities_names)):
    print(position)
    
for position in range(len(cities_names)):
    cities_names [position] = "Rio de Janeiro"
print(cities_names)

print(list(range(10)))
print(list(range(2, 10)))
print(list(range(2, 10, 2)))