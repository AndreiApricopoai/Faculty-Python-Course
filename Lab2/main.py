from math import sqrt


# Laboratory 2
# Ex1 - Write a function to return a list of the first n numbers in the Fibonacci string.
def fibonacci(n: int) -> list:
    if n <= 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]

    result = [0, 1]
    for i in range(2, n):
        result.append(result[i - 1] + result[i - 2])
    return result


print(fibonacci(10))


# Ex2 - Write a function that receives a list of numbers and returns a list of the prime numbers found in it.
def is_prime(n: int) -> bool:
    prime_flag = 0

    if n > 1:
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                prime_flag = 1
                break
        if prime_flag == 0:
            return True
        else:
            return False
    else:
        return False


def prime_list(numbers: list) -> list:
    result = []
    for number in numbers:
        if is_prime(number):
            result.append(number)
    return result


numbers_list = [2, 3, 4, 5, 16, 17, 18, 19, 20, 23]
print(prime_list(numbers_list))


# Ex3 - Write a function that receives as parameters two lists a and b and returns:
# (a intersected with b, a reunited with b, a - b, b - a)

def list_operations(a: list, b: list) -> tuple:
    a_set = set(a)
    b_set = set(b)

    intersection = list(a_set & b_set)
    union = list(a_set | b_set)
    a_diff_b = list(a_set - b_set)
    b_diff_a = list(b_set - a_set)

    return (intersection, union, a_diff_b, b_diff_a)


a = [1, 2, 3, 4, 5]
b = [4, 5, 6, 7, 8]

print(list_operations(a, b))


# Ex4 - Write a function that receives as a parameters a list of musical notes
# (strings), a list of moves (integers) and a start position (integer).
# The function will return the song composed by going through the musical notes beginning
# with the start position and following the moves given as parameter.
# Example : compose(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2) will return
# ["mi", "fa", "do", "sol", "re"]
def compose(notes: list, moves: list, start_position: int) -> list:
    result = [notes[start_position]]
    notes_length = len(notes)
    for move in moves:
        start_position = (start_position + move) % notes_length
        result.append(notes[start_position])
    return result


print(compose(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2))


# Ex5 - Write a function that receives as parameter a matrix and will return
# the matrix obtained by replacing all the elements under the main diagonal with 0 (zero).
def replace_under_main_diagonal(matrix: list[list[int]]) -> list[list[int]]:
    n = len(matrix)
    m = len(matrix[0])

    if n != m:
        return matrix

    for i in range(n):
        for j in range(m):
            if i > j:
                matrix[i][j] = 0
    return matrix


mat = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(replace_under_main_diagonal(mat))


# Ex6 - Write a function that receives as a parameter a variable number of lists and a whole
# number x. Return a list containing the items that appear exactly x times in the incoming lists.
def items_x_times(x: int, *lists: list) -> list:
    result = []
    freq = {}

    for list in lists:
        for item in list:
            if item in freq:
                freq[item] = freq[item] + 1
            else:
                freq[item] = 1

    for key in freq.keys():
        if freq[key] == x:
            result.append(key)

    return result


print(items_x_times(2,[1,2,3], [2,3,4],[4,5,6], [4,1, "test"]))


# Ex7 - Write a function that receives as parameter a list of numbers (integers) and will
# return a tuple with 2 elements. The first element of the tuple will be the number of
# palindrome numbers found in the list and the second element will be the greatest palindrome number.
def is_palindrome(n: int) -> bool:
    s = str(n)
    return s == s[::-1]


def number_and_max_palindrome(numbers: list[int]) -> tuple:
    count = 0
    max_palindrome = -1

    for number in numbers:
        if is_palindrome(number):
            count = count + 1
            if number > max_palindrome:
                max_palindrome = number

    return (count, max_palindrome)


print(number_and_max_palindrome([123, 11, 121, 12]))


# Ex8 - Write a function that receives a number x, default value equal to 1, a list of strings,
# and a boolean flag set to True. For each string, generate a list containing the characters
# that have the ASCII code divisible by x if the flag is set to True, otherwise it should
# contain characters that have the ASCII code not divisible by x.

def ascii_divisible(x: int = 1, strings: list[str] = [], flag: bool = True) -> list[list[str]]:
    result = []
    for string in strings:
        temp = []
        for character in string:
            if flag:
                if ord(character) % x == 0:
                    temp.append(character)
            else:
                if ord(character) % x != 0:
                    temp.append(character)
        result.append(temp)
    return result


print(ascii_divisible(2,  ["test", "hello", "lab002"], flag=False))


# Ex9 - Write a function that receives as paramer a matrix which represents the heights
# of the spectators in a stadium and will return a list of tuples (line, column) each one
# representing a seat of a spectator which can't see the game. A spectator can't see the
# game if there is at least one taller spectator standing in front of him. All the seats are occupied.
# All the seats are at the same level. Row and column indexing starts from 0, beginning with the closest
# row from the field.
def bad_seats(matrix: list[list[int]]) -> list[tuple]:
    result = []
    n = len(matrix)
    m = len(matrix[0])

    for i in range(n-1, -1, -1):
        for j in range(m):
            for k in range(i-1, -1, -1):
                if matrix[k][j] >= matrix[i][j]:
                    result.append((i, j))
                    break
    return result


print(bad_seats([[1, 2, 3, 2, 1, 1],
                [2, 4, 4, 3, 7, 2],
                [5, 5, 2, 5, 6, 4],
                [6, 6, 7, 6, 7, 5]]))


# Ex10 - Write a function that receives a variable number of lists and returns a list
# of tuples as follows: the first tuple contains the first items in the lists,
# the second element contains the items on the position 2 in the lists, etc.
def tuples_from_lists(*lists: list) -> list[tuple]:
    result = []
    max_length = 0
    for list in lists:
        if len(list) > max_length:
            max_length = len(list)

    for i in range(max_length):
        temp_list = []
        for list in lists:
            if i < len(list):
                temp_list.append(list[i])
            else:
                temp_list.append(None)
        result.append(tuple(temp_list))
    return result


print(tuples_from_lists([1,2,3,4], [5,6,7], ["a", "b", "c"]))


# Ex11 - Write a function that will order a list of string tuples based on the 3rd
# character of the 2nd element in the tuple.
# Example: ('abc', 'bcd'), ('abc', 'zza')] ==> [('abc', 'zza'), ('abc', 'bcd')]
def sort_tuples(tuples: list[tuple]) -> list[tuple]:
    return sorted(tuples, key=lambda x: x[1][2])


print(sort_tuples([('abc', 'bcd'), ('abc', 'zza')]))


# Ex12 - Write a function that will receive a list of words as parameter and will
# return a list of lists of words, grouped by rhyme. Two words rhyme if both of them
# end with the same 2 letters.Example:group_by_rhyme(['ana', 'banana', 'carte', 'arme', 'parte'])
# will return [['ana', 'banana'], ['carte', 'parte'], ['arme']]
def group_by_rhyme(words: list[str]) -> list[list[str]]:
    result = []
    while len(words) > 0:
        temp = []
        ending = words[0][-2:]
        to_remove = []
        for word in words:
            if word[-2:] == ending:
                temp.append(word)
                to_remove.append(word)
        for word in to_remove:
            words.remove(word)
        result.append(temp)
    return result


print(group_by_rhyme(['ana', 'banana', 'carte', 'arme', 'parte']))