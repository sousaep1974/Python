import csv

with open('letscode-suzano/brasil_covid.csv', 'r') as csv_file:
    reader = csv.reader(csv_file) 
    header = next(reader) #skip document header 
    for line in reader:
        if float(line[2]) > 1:
            print(line)
            
with open('letscode-suzano/brasil_covid.csv', 'r') as csv_file:
    lines = csv_file.read()
    lines = lines.split('\n')
    for line in lines:
        line = lines.split(",")
        print(lines)

with open ("users.csv", "w", newline="") as users_file:
    whiter_file = csv.writer(users_file)
    whiter_file.writerow(["name", "lastName", "email", "genre"])
    whiter_file.writerow(["Edivan", "Sousa", "sousaep1974@gmail.com", "male"])
    
header = ['name', 'lastName']
datas = []
opt = input ('O que deseja fazer?\n1 - cadastrar\n0 - Sair\n')
while opt != '0':
    name = input('Qual seu nome?')
    lastName = input ('Qual seu sobrenome?')
    datas.append([name, lastName])
    opt = input ('O que deseja fazer?\n1 - cadastrar\n0 - Sair\n')
print(datas)

with open('users.csv', "w", newline='') as file_csv:
    writer = csv.writer(file_csv)
    writer.writerow(header)
    writer.writerows(datas)
    
with open ('users.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        print(row)