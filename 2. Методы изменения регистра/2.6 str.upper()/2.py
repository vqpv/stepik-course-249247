s = input()

print(*(i[0].upper() for i in list(s.split()) if len(i) > 1), sep="")
