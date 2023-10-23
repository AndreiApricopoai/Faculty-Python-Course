# Laboratory 3

# Ex1 - Write a function that receives as parameters two lists a and b
# and returns a list of sets containing: (a intersected with b, a reunited with b, a - b, b - a)
def list_operations(a: list, b:list) -> tuple:
    a_set = set(a)
    b_set = set(b)

    intersection = list(a_set & b_set)
    union = list(a_set | b_set)
    a_minus_b = list(a_set - b_set)
    b_minus_a = list(b_set - a_set)

    return intersection, union, a_minus_b, b_minus_a


a = [1, 2, 3, 4, 5]
b = [4, 5, 6, 7, 8]

print(list_operations(a, b))


# Ex2 - Write a function that receives a string as a parameter and returns
# a dictionary in which the keys are the characters in the character string
# and the values are the number of occurrences of that character in the given text.
def character_occurrences(input_string: str) -> dict[str, int]:
    result = {}
    for character in input_string:
        if character in result.keys():
            result[character] = result[character] + 1
        else:
            result[character] = 1
    return result


print(character_occurrences("Ana has apples."))


# Ex3 - Compare two dictionaries without using the operator "==" returning True or False.
# (Attention, dictionaries must be recursively covered because they can contain other
# containers, such as dictionaries, lists, sets, etc.)
def compare_dictionaries(dict1: dict, dict2: dict) -> bool:
    if isinstance(dict1, dict) and isinstance(dict2, dict):
        if set(dict1.keys()) != set(dict2.keys()):
            return False

        for key in dict1:
            if not compare_dictionaries(dict1[key], dict2[key]):
                return False

        return True
    else:
        return dict1 == dict2


dict_b = {'a': 1, 'b': {'c': 2, 'd': [3, 4]}}
dict_a = {'a': 1, 'b': {'c': 2, 'd': [3, 4]}}
dict_c = {'a': 2, 'b': {'c': 2, 'd': [3, 5]}}

result_ab = compare_dictionaries(dict_a, dict_b)
result_ac = compare_dictionaries(dict_a, dict_c)

print(result_ab)  # True
print(result_ac)  # False


# Ex4 - The build_xml_element function receives the following parameters: tag, content,
# and key-value elements given as name-parameters. Build and return a string that represents
# the corresponding XML element. Example: build_xml_element
# ("a", "Hello there", href =" http://python.org ", _class =" my-link ", id= " someid ")
# returns  the string = "<a href=\"http://python.org \ "_class = \" my-link \ "id = \" someid \ "> Hello there </a>"
def build_xml_element(tag: str, content: str, **kwargs) -> str:
    result = "<" + tag + " "
    for key in kwargs:
        if isinstance(kwargs[key], str):
            result = result + key + "=\"" + kwargs[key] + "\" "
    result = result + ">" + content + "</" + tag + ">"
    return result


print(build_xml_element("a", "Hello there",
                        href="http://python.org",
                        _class="my-link",
                        id="someid"))


# Ex5 - The validate_dict function that receives as a parameter a set of tuples
# (that represents validation rules for a dictionary that has strings as keys and values)
# and a dictionary. A rule is defined as follows: (key, "prefix", "middle", "suffix").
# A value is considered valid if it starts with "prefix", "middle" is inside the value
# (not at the beginning or end) and ends with "suffix". The function will return True
# if the given dictionary matches all the rules, False otherwise.
def validate_dict(rules: set[tuple[str, str, str, str]], dictionary: dict[str, str]) -> bool:
    for rule in rules:
        if rule[0] not in dictionary.keys():
            return False
        if not dictionary[rule[0]].startswith(rule[1]):
            return False
        if rule[2] not in dictionary[rule[0]][len(rule[1]):len(dictionary[rule[0]]) - len(rule[3])]:
            return False
        if not dictionary[rule[0]].endswith(rule[3]):
            return False
    return True


rules = {("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}
data = {"key1": "come inside, it's too cold out", "key3": "this is not valid"}

result = validate_dict(rules, data)
print(result)  # Should print False


# Ex6 - Write a function that receives as a parameter a list and returns a tuple (a, b),
# representing the number of unique elements in the list, and b representing the number
# of duplicate elements in the list (use sets to achieve this objective).
def count_unique_duplicate_elements(input_list: list) -> tuple[int, int]:
    unique_elements = set(input_list)
    duplicate_elements = len(input_list) - len(unique_elements)
    return len(unique_elements), duplicate_elements


example_list = [1, 2, 3, 4, 2, 5, 6, 3, 7]
result = count_unique_duplicate_elements(example_list)
print(result)


# Ex7 - Write a function that receives a variable number of sets and returns a dictionary with
# the following operations from all sets two by two: reunion, intersection, a-b, b-a.
# The key will have the following form: "a op b", where a and b are two sets,
# and op is the applied operator: |, &, -.
def set_operations(*sets: set) -> dict[str, set]:
    result = {}
    for i in range(len(sets)):
        for j in range(i + 1, len(sets)):
            result[str(sets[i]) + " | " + str(sets[j])] = sets[i] | sets[j]
            result[str(sets[i]) + " & " + str(sets[j])] = sets[i] & sets[j]
            result[str(sets[i]) + " - " + str(sets[j])] = sets[i] - sets[j]
    return result


print(set_operations({1,2}, {2, 3}))


# Ex8 - Write a function that receives a single dict parameter named mapping.
# This dictionary always contains a string key "start". Starting with the value of this key
# you must obtain a list of objects by iterating over mapping in the following way: the value
# of the current key is the key for the next value, until you find a loop (a key that was visited before).
# The function must return the list of objects obtained as previously described.
def loop(mapping: dict[str, str]) -> list[str]:
    result = []
    current_key = mapping['start']
    while current_key not in result:
        result.append(current_key)
        current_key = mapping[current_key]
    return result


print(loop({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}))


# Ex9 - Write a function that receives a variable number of positional arguments and a variable
# number of keyword arguments and will return the number of positional arguments whose values
# can be found among keyword arguments values.
def positional_keywords_counter(*positionals, **keywords) -> int:
    count = 0
    for positional in positionals:
        if positional in keywords.values():
            count = count + 1
    return count


print(positional_keywords_counter(1, 2, 3, 4, x=1, y=2, z=3, w=5))