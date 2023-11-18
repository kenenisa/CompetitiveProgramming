s = input()
def allUp():
    valid = True
    for i in s[1:]:
        if i.islower():
            valid =False
            break
    return valid
if allUp():
    if s[0].isupper():
        print(s.lower())
    else:
        print(s[:1].upper() + s[1:].lower())
else:
    print(s)