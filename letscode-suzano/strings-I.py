empresa = 'Google'
print(empresa)

empresa = "Google"
print(empresa)

#Erro
#empresa = 'Let's Code' 
#print(empresa)

empresa = "Let's Code"
print(empresa)

frase = "O professor disse: \"Hoje a pizza é por minha conta\""
print(frase)

empresa = "Google"
print(empresa[0])
print(empresa[0:3])

#Split
cities_names = "São Paulo, Belo Horizonte, Rio de Janeiro, Brasília"
cities_names = cities_names.split(", ")
print(cities_names)

#Strip
header = "                 MENU PRINCIPAL                            "
print(header.strip())

city_name = "rIo dE jaNEIiro"
print(city_name) 
print(city_name.title()) # Rio De Janeiro
print(city_name.capitalize()) # Rio de Janeiro
print(city_name.lower()) # rio de janeiro
print(city_name.upper()) # RIO DE JANEIRO

city_name1 = input("Qual cidade do Brasil é conhecida como cidade maravilhosa?")
city_name1 = city_name1.strip()
while city_name1.lower() !="rio de janeiro": 
    print("Tenta de novo, vai!")
    city_name1 = input("Qual cidade do Brasil é conhecida como cidade maravilhosa?")
print("Booa, campeão!")

message = "Você viu o que o prfessor Edivan falou na sla ontem?"
IWas_quoted = "Edivan" in message
print(IWas_quoted)
