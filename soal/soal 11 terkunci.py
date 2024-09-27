s = input()
simpan = ""

for i in range(len(s)):
    if s[i] in simpan:
        continue
    else:
        if s[i] == " ":
            continue
        else:
                simpan += s[i]
print(simpan) 