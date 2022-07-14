def hello():
    print("Hello, World!")
hello()
# ------------------------------------------------


def calculate_average(value1, value2, value3):
    sum = value1 + value2 + value3
    media = sum / 3
    return media
result = calculate_average(10, 10, 10)
print(result)
result2 = calculate_average(value1 = 9, value2 = 10, value3 = 9)
print(result2)
# ------------------------------------------------

def summation(list):
    sum = 0
    for item in list:
        sum = sum + item
    return sum

# ------------------------------------------------

numbers = [1, 2, 3, 4, 5]
sum_of_numbers = summation(numbers)
print("A soma dos elementos da lista vale: ", sum_of_numbers)

if summation(numbers) > 50:
    print("Que soma grande!")
else:
    print("Que soma pequena!")

# ------------------------------------------------


def recursive_function(numbers):
    if (numbers != 1):
        recursive_function(numbers - 1)
    print(numbers)


print("Testando a função recursiva:")
recursive_function(10)
