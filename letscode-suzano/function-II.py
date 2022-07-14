def calculate_average(value1, value2, value3):
    sum1 = value1 + value2 + value3
    average = sum1 / 3
    return average

def calculate_average(*args, margin):
    sum1 = sum(args)
    average = sum1 / len(args)
    return average + margin

print(calculate_average(10, 8, 9, margin=0.3))

def print_info(**kwargs):
    print (kwargs, type(kwargs))
    
print_info(name="Edivan", last_name="Sousa")