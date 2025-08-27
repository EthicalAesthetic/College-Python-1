def pyramid(rows):
    for i in range(1, rows + 1):
        # Print spaces
        print(' ' * (rows - i), end='')
        # Print stars
        print('*' * (2 * i - 1))

def reverse_pyramid(rows):
    for i in range(rows, 0, -1):
        # Print spaces
        print(' ' * (rows - i), end='')
        # Print stars
        print('*' * (2 * i - 1))

def main():
    try:
        rows = int(input("Enter the number of rows for the pyramid: "))
        print("\nPyramid:")
        pyramid(rows)
        print("\nReverse Pyramid:\n")
        reverse_pyramid(rows)
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
