s = input()

if len(s) > 3:
    print(s[:3] + s[3:].lower())
else:
    print(s)
