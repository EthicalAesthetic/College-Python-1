def frequency_of_char(s, char):
    """Find the frequency of a character in a string."""
    return s.count(char)

def replace_char(s, old_char, new_char):
    """Replace a character by another character in a string."""
    return s.replace(old_char, new_char)

def remove_first_occurrence(s, char):
    """Remove the first occurrence of a character from a string."""
    index = s.find(char)
    if index == -1:
        return s  # char not found
    return s[:index] + s[index+1:]

def remove_all_occurrences(s, char):
    """Remove all occurrences of a character from a string."""
    return s.replace(char, '')

# Taking inputs from user
string = input("Enter the initial string: ")
print(f"Current string: {string}")

char_to_find = input("Enter the character to find frequency: ")
freq = frequency_of_char(string, char_to_find)
print(f"Frequency of '{char_to_find}': {freq}")

old_char = input("Enter the character to replace: ")
new_char = input("Enter the new character: ")
string = replace_char(string, old_char, new_char)
print(f"String after replacing '{old_char}' with '{new_char}': {string}")

char_to_remove_first = input("Enter the character to remove first occurrence: ")
string = remove_first_occurrence(string, char_to_remove_first)
print(f"String after removing first occurrence of '{char_to_remove_first}': {string}")

char_to_remove_all = input("Enter the character to remove all occurrences: ")
string = remove_all_occurrences(string, char_to_remove_all)
print(f"String after removing all occurrences of '{char_to_remove_all}': {string}")
