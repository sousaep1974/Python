file = open('letscode-suzano/dom_casmurro_cap_1.txt', 'r')
text = file.read()
print(text)
file.close()

file = open('letscode-suzano/dom_casmurro_cap_1.txt', 'r')
line = file.readline()
while line != "":
    print(line, end="")
    line = file.readline()
file.close()

file = open('letscode-suzano/dom_casmurro_cap_1.txt', 'r')
for line in file:
    print(line, end="")
file.close()

with open('letscode-suzano/dom_casmurro_cap_1.txt', 'r') as file:
    text = file.read()
    print(text)

file.read() 

with open("letscode-suzano/file_test.txt", "w") as file:
    file.write("A primeira linha que escrevi usando Python\n")
    file.write("A segunda linha que escrevi usando Python\n")
    
with open("letscode-suzano/file_test.txt", "a") as file:
    file.write("A terceira linha que escrevi usando Python\n")
    
with open("file_test.txt", "r") as file:
    print(file.read(), end="")
    
    