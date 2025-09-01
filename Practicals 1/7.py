def find_all_occurrences(s, sub):
    indices = []
    start = 0
    while True:
        # Find the substring starting from the current index 'start'
        index = s.find(sub, start)
        if index == -1:
            break
        indices.append(index)
        start = index + 1  # Move start to the next position after the found substring
    return indices if indices else -1

# Example usage:
string = input("Enter the main string: ")
substring = input("Enter the substring to find: ")

result = find_all_occurrences(string, substring)
print("Indices of all occurrences:", result)
