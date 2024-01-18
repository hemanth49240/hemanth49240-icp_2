def fln(fe, le):
    return f"{fe} {le}"

def string_alternative(fu):
    s=''
    for n in range(len(fu)):
        if n%2==1:
            s=s+fu[n]
    return s

fe = input("Enter your first name:\n")
le = input("Enter your last name:\n")
fu = fln(fe, le)
print(fu)
print(string_alternative(fu))
