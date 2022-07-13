city_data = {
    "name": "São Paulo",
    "state": "São Paulo",
    "area_km2": 1521,
    "population_millions" : 12.18}
print(type(city_data))
print(city_data)
city_data["country"] = "Brasil" #Add 
print(city_data)
city_data["area_km2"] = "1500" #Alter 
print(city_data)

news_datas = {
    "population_millions" : "15",
    "foundation" : "25/01/1554",
}

city_data.update(news_datas)
print(city_data)
print(city_data.get("prefeito"))

print(city_data.keys()) #retorna uma lista de chaves de um dicionário
print("_ _ _ _")
print(city_data.values()) #retorna uma lista de valores de um dicionário
print("_ _ _ _")
print(city_data.items()) #retorna uma lista de tuplas (chave, valor) de um dicionário
