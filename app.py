# Project: Caesar Cipher Program
# Objective:
# Write a Caesar Cipher program that allows the user to encrypt and decrypt messages. The program should:
# Ask the user if they want to encrypt or decrypt a message.
# Ask for the message and the shift value.
# Encrypt or decrypt the message accordingly.

import string

lower = string.ascii_lowercase
upper = string.ascii_uppercase

def caesar_encrypt(message, shift):
    encrypted_message = ""
    for char in message:
        if char in lower:
            new_index = (lower.index(char) + shift) % 26
            encrypted_message += lower[new_index]
        elif char in upper:
            new_index = (upper.index(char) + shift) % 26
            encrypted_message += upper[new_index]
        else:
            encrypted_message += char
    return encrypted_message

def caesar_decrypt(encrypted_message, shift):
    decrypted_message = ""
    for char in encrypted_message:
        if char in lower:
            new_index = (lower.index(char) - shift) % 26
            decrypted_message += lower[new_index]
        elif char in upper:
            new_index = (upper.index(char) - shift) % 26
            decrypted_message += upper[new_index]
        else:
            decrypted_message += char
    return decrypted_message

# print(caesar_encrypt('hello', 4))

# print(caesar_decrypt('lipps', 4))

user_input = input("Hi, would like to encrypt or decrypt: \n")

if user_input == "encrypt":
    message = input("Enter the message you want to encrypt: ")
    shift = int(input("Enter the shift value: "))
    print(caesar_encrypt(message, shift))
elif user_input == "decrypt":
    message = input("Enter the message you want to decrypt: ")
    shift = int(input("Enter the shift value: "))
    print(caesar_decrypt(message, shift))
else:
    print("Invalid task inputted, select between 'Encrypt' and 'Decrypt'")

if_continue = input("Do you want to continue using Caesar Cipher? (yes/no)")
if if_continue.lower() == "no":
    to_continue = False
else:
    to_continue = True

