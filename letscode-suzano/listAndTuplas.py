country_names = ["Brasil", "Argentina", "China", "Canadá", "Japão"]
print(country_names)
print("Tamanho da lista", len(country_names))
print("País: ", country_names[4])
print("País: ", country_names[-1])
country_names[4] = "Colômbia"
print("País: ", country_names[4])
print(country_names)
print(country_names[1:3])
print(country_names[1:-1])
print(country_names[2:])
print(country_names[:3])
print(country_names[:])
print(country_names[::2])
print(country_names[::-1])
print("Brasil" in country_names)
print("Canadá" not in country_names)

capital_list = []
capital_list.append("Brasília")
capital_list.append("Buenos Aries")
capital_list.append("Pequin")
capital_list.append("Bogotá")
print(capital_list)

capital_list.insert(2,"París")
print(capital_list)

capital_list.remove("Buenos Aries")
print(capital_list)

removido = capital_list.pop(2)
print(capital_list, removido)

country_names = ("Brasil", "Argentina", "China", "Canadá", "Japão")
print(country_names, type(country_names))

country_names = "Brasil", "Argentina", "China", "Canadá", "Japão"
print(country_names, type(country_names))

state_names = "São Paulo",
print(state_names, type(state_names))
len(country_names)
country_names[0]
b, a, c, ca, j = country_names
print(b, c, j)
print(* country_names)


