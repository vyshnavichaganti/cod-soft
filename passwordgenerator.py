import random
length = int(input("Enter password length: "))

characters = "@abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
password = ""
for i in range(length):
    password += random.choice(characters)
print("Your password is:", password)
