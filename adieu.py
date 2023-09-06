import inflect

names = []
names_last = []

while True:
    try:
        name = input("")
        names.append(name)
    except EOFError:
        break

if len(names) == 1:
    print(f"Adieu, adieu, to {names[0]}")
elif len(names) == 2:
    for i in range(len(names) - 1):
        names_last.append(names[i])
    frase = ", ".join(names_last)
    print(f"Adieu, adieu, to {frase} and {names[len(names) - 1]}")
    
else:
    for i in range(len(names) - 1):
        names_last.append(names[i])

    frase = ", ".join(names_last)
    print(f"Adieu, adieu, to {frase}, and {names[len(names) - 1]}")
