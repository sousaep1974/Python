idade = input("Informe a sua idade: ")
print(idade, type(idade))

idade = int(idade)
print(idade, type(idade))

monthly_salary = input("Digite o valor do seu sálario mensal: ")
monthly_salary = float(monthly_salary)

monthly_spent = input("Digite o valor do seu gasto mensal: ")
monthly_spent = float(monthly_spent)

total_salary = monthly_salary * 12
total_spent = monthly_spent * 12

amount_saved = total_salary - total_spent

print('O montante que você pode economizar é de ', amount_saved)