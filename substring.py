s = input("Enter string: ")

longest = ""

for i in range(len(s)):
    sub = ""

    for j in range(i, len(s)):
        if s[j] not in sub:
            sub = sub + s[j]
        else:
            break

    if len(sub) > len(longest):
        longest = sub

print("Longest Substring:", longest)
print("Length:", len(longest))