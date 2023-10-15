# Laboratory 1

# Ex1 - Find The greatest common divisor of multiple numbers read from the console.
def gcd_for_two_numbers(x, y):
    while y != 0:
        temp = x % y
        x = y
        y = temp
    return x


def gcd_for_list_of_numbers(numbers):
    result = numbers[0]
    for i in range(1, len(numbers)):
        result = gcd_for_two_numbers(result, numbers[i])
    return result

numbers_count = int(input("How many numbers do you want to input? "))
numbers = []
for i in range(numbers_count):
    number = int(input("Input number: "))
    numbers.append(number)
print("The greatest common divisor is: ", gcd_for_list_of_numbers(numbers))


# Ex2 - Write a script that calculates how many vowels are in a string.
def count_vowels(input_string):
    vowels = "aeiouAEIOU"
    count = 0
    for i in range(len(input_string)):
        if input_string[i] in vowels:
            count = count + 1
    return count


user_input = input("Input string: ")
print("The number of vowels in your string is: ", count_vowels(user_input))


# Ex3 - Write a script that receives two strings
# and prints the number of occurrences of the first string in the second.
def count_occurrences(substring, string):
    count = 0
    for i in range(len(string)):
        if string[i:i + len(substring)] == substring:
            count = count + 1
    return count


user_substring = input("Input substring: ")
user_string = input("Input string: ")
print("The number of occurrences of the first string in the second is: ",
      count_occurrences(user_substring, user_string))


# Ex4 - Write a script that converts a string of characters
# written in UpperCamelCase into lowercase_with_underscores.
def convert_to_lowercase_with_underscores(input_string):
    result = input_string[0].lower()
    for i in range(1, len(input_string)):
        if input_string[i].isupper():
            result = result + "_" + input_string[i].lower()
        else:
            result = result + input_string[i]
    return result


user_string = input("Input a UpperCamelCase string: ")
print("The string converted to lowercase_with_underscores is: ",
      convert_to_lowercase_with_underscores(user_string))


# Ex5 - Given a square matrix of characters, write a script that prints
# the string obtained by going through the matrix in spiral order
def spiral_order(matrix):
    result = ""
    n = len(matrix)
    bottom = 0; top = n - 1; left = 0; right = n - 1

    while bottom <= top and left <= right:
        for i in range(left, right + 1):
            result = result + matrix[bottom][i]
        bottom = bottom + 1

        for i in range(bottom, top + 1):
            result = result + matrix[i][right]
        right = right - 1

        if bottom <= top:
            for i in range(right, left - 1, -1):
                result = result + matrix[top][i]
        top = top - 1

        if left <= right:
            for i in range(top, bottom - 1, -1):
                result = result + matrix[i][left]
        left = left + 1

    return result


matrix_example = [
    ['f', 'i', 'r', 's'],
    ['n', '_', 'l', 't'],
    ['o', 'b', 'a', '_'],
    ['h', 't', 'y', 'p']
]

print(spiral_order(matrix_example))


# Ex6 - Write a function that validates if a number is a palindrome.
def is_number_palindrome(number):
    copy = number
    reversed_number = 0
    while copy > 0:
        reversed_number = reversed_number * 10 + copy % 10
        copy = copy // 10
    if reversed_number == number:
        return True
    else:
        return False


print(is_number_palindrome(12321))
print(is_number_palindrome(12345))


# Ex7 - Write a function that extract a number from a text
def extract_number_from_text(text):
    number = ""
    for char in text:
        if char.isdigit():
            number = number + char
        elif number != "":
            break
    return int(number)


print(extract_number_from_text("An apple is 123 USD"))


# Ex8 - Write a function that counts how many bits with value 1 a number has.
# For example for number 24, the binary format is 00011000, meaning 2 bits with value "1"
def count_bits(number):
    count = 0
    while number > 0:
        if number % 2 == 1:
            count = count + 1
        number = number // 2
    return count


print(count_bits(24))


# Ex9 - Write a functions that determine the most common letter in a string.
def most_common_letter(text):
    text = text.lower()

    letters = []
    for i in text:
        if i.isalpha():
            letters.append(i)

    count = {}
    for letter in letters:
        if letter in count:
            count[letter] = count[letter] + 1
        else:
            count[letter] = 1

    max_letter = ''
    max_count = 0

    for item in count:
        if count[item] > max_count:
            max_letter = item
            max_count = count[item]
    return max_letter


print(most_common_letter("an apple is not a tomato"))


# Ex10 - Write a function that counts how many words exists in a text. A text is considered to be form
# out of words that are separated by only ONE space. For example: "I have Python exam" has 4 words.
def word_count(text):
    return len(text.split())


print(word_count("I have Python exam"))