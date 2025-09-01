def swap_first_n_chars(str1, str2, n):
    # Handle the case where n is larger than either string's length
    n = min(n, len(str1), len(str2))
    
    # Swap the first n characters
    new_str1 = str2[:n] + str1[n:]
    new_str2 = str1[:n] + str2[n:]
    
    return new_str1, new_str2

# Taking inputs from the user
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
n = int(input("Enter the number of characters to swap from the start: "))

swapped_str1, swapped_str2 = swap_first_n_chars(string1, string2, n)
print(f"After swapping first {n} characters:")
print(f"First string: {swapped_str1}")
print(f"Second string: {swapped_str2}")
