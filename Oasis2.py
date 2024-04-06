import random
import string

length_of_the_password = int(input("Enter the length of the password: "))

characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(characters) for _ in range(length_of_the_password))

print("Your generated password is:", password)