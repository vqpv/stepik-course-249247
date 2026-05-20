s = input()

print(*list(map(str.title, s.split("; "))), sep="\n")
