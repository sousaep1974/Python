counter = 0
while counter < 10:
    counter = counter + 1
    if counter == 1:
        print (counter, "item limpo")
    else:
        print(counter, "Itens limpos")
        
print("Fim da repetição do bloco while")

text = input("Digite a sua senha: ")
while text != "LetsCode":
    text = input("Senha inválida. Tente novamente.")
print("Acesso permitido")
