from collections import Counter

with open("input.txt", "r") as in_file:
    lines = in_file.readlines()
word_counts = Counter(word for line in lines for word in line.strip().split())

with open("output.txt", "w") as out_file:
    out_file.writelines(lines)
    out_file.write("\nWord_count:\n")
for word, count in word_counts.items():
    with open("output.txt", "a") as out_file:
        out_file.write(f"{word}: {count}\n")
    print(f"{word}: {count}")

print("Word count saved in op file")
