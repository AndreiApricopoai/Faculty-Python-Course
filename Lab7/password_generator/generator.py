import random
import string


def generate_password(length=8, use_special_chars=True, use_numbers=True, use_mixed_case=True):
    password_characters = ''
    password_characters += string.ascii_lowercase

    if use_mixed_case:
        password_characters += string.ascii_uppercase

    if use_numbers:
        password_characters += string.digits

    if use_special_chars:
        password_characters += string.punctuation

    password = []
    for i in range(length):
        random_character = random.choice(password_characters)
        password.append(random_character)

    password_string = ''.join(password)
    return password_string
