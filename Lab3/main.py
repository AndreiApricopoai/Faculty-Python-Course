

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

    return (intersection, union, a_minus_b, b_minus_a)


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

