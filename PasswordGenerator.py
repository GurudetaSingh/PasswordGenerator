import random
import string

# All printable ASCII characters excluding whitespace
characters = list(string.printable.strip())

def generate_random_password():
    result = [] 
    length_of_password = int(input("Please enter the length for the password."))

    random.shuffle(characters) 

    for i in range(length_of_password):
        result.append(random.choice(characters)) 

    random.shuffle(characters) 

    return "".join(result) 

print(generate_random_password())




