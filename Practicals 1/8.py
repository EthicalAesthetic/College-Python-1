def cubes_of_even_for_loop(input_list):
    result = []
    for item in input_list:
        if isinstance(item, int) and item % 2 == 0:
            result.append(item ** 3)
    return result

def cubes_of_even_list_comp(input_list):
    return [item ** 3 for item in input_list if isinstance(item, int) and item % 2 == 0]

# Input function to read list elements from the user
def input_list():
    print("Enter the elements of the list separated by space:")
    elements = input().split()
    processed_list = []
    for el in elements:
        # Try to convert to int, else keep as string
        try:
            processed_list.append(int(el))
        except ValueError:
            try:
                processed_list.append(float(el))
            except ValueError:
                processed_list.append(el)  # keep as string if not number
    return processed_list

# Main program
user_list = input_list()
print("Input list:", user_list)

print("Cubes of even integers (for loop):", cubes_of_even_for_loop(user_list))
print("Cubes of even integers (list comprehension):", cubes_of_even_list_comp(user_list))
