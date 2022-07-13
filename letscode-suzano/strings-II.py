cumprimento = "Olá, "
nome = "Edivan"
print(cumprimento + nome)
print(nome * 5)

nome = "Edivan"
idade = 48
n_filhos = 3
print(nome + " tem " + str(idade) + " anos e " + str(n_filhos) + " filhos") 
print ("{} tem {} anos e {} filhos".format(nome, idade, n_filhos)) # Método format()
print (f"{nome} tem {idade} anos e {n_filhos} filhos") # Atalho do método format()

petrol_price = 3.476
print("O preço da gasolina hoje está R$ {:.2f}".format(petrol_price))