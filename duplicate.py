text = input("Enter string: ")

result = ""

for ch in text:
    found = False

    for r in result:
        if ch == r:
            found = True
            break

    if not found:
        result = result + ch

print("After removing duplicates:", result)