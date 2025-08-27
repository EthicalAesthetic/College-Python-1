def analyze_file(filename):
    char_count = 0
    word_count = 0
    line_count = 0
    char_freq = {}

    lines = []
    
    # Read the file
    with open(filename, 'r') as file:
        for line in file:
            lines.append(line.rstrip('\n'))
            line_count += 1
            char_count += len(line)  # includes newline chars
            words = line.split()
            word_count += len(words)
            
            # Count frequency of each character
            for ch in line:
                if ch in char_freq:
                    char_freq[ch] += 1
                else:
                    char_freq[ch] = 1

    # a. Print total counts
    print(f"Total characters (including newlines): {char_count}")
    print(f"Total words: {word_count}")
    print(f"Total lines: {line_count}")

    # b. Print character frequency
    print("\nCharacter frequency:")
    for ch, freq in sorted(char_freq.items()):
        # For better visibility, replace newline and space characters with labels
        if ch == '\n':
            display_ch = '\\n'
        elif ch == ' ':
            display_ch = "' '"
        else:
            display_ch = ch
        print(f"{display_ch}: {freq}")

    # c. Print words in reverse order
    all_words = []
    for line in lines:
        all_words.extend(line.split())
    print("\nWords in reverse order:")
    print(' '.join(all_words[::-1]))

    # d. Copy even lines to 'File1', odd lines to 'File2'
    with open('File1.txt', 'w') as file1, open('File2.txt', 'w') as file2:
        for i, line in enumerate(lines, start=1):
            if i % 2 == 0:
                file1.write(line + '\n')
            else:
                file2.write(line + '\n')

    print("\nLines copied to 'File1.txt' (even lines) and 'File2.txt' (odd lines).")

# Usage example
filename = input("Enter the filename to analyze: ")
try:
    analyze_file(filename)
except FileNotFoundError:
    print("File not found. Please check the filename and try again.")
