# Loop with numbers and letters

word = input("Enter a word: ")

print("\n Letters with numbering: ")

for i, letter in enumerate (word, start = 1):
    print(f"{i}. {letter}")

# Print how many letters the word has
print(f"\n the word has {len(word)}")