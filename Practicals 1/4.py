def analyze_char(ch):
    digit_names = {
        '0': 'ZERO', '1': 'ONE', '2': 'TWO', '3': 'THREE', '4': 'FOUR',
        '5': 'FIVE', '6': 'SIX', '7': 'SEVEN', '8': 'EIGHT', '9': 'NINE'
    }

    if ch.isalpha():
        print(f"'{ch}' is a letter.")
        if ch.isupper():
            print("It is uppercase.")
        else:
            print("It is lowercase.")
    elif ch.isdigit():
        print(f"'{ch}' is a numeric digit.")
        print(f"Its name is: {digit_names[ch]}")
    else:
        print(f"'{ch}' is a special character.")

def main():
    ch = input("Enter a single character: ")
    if len(ch) != 1:
        print("Please enter exactly one character.")
    else:
        analyze_char(ch)

if __name__ == "__main__":
    main()
