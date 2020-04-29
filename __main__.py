from random import choice

import names

itstime = False

print("Welcome to Fantasy Name Generator!\n\nM - male name\nF - female name\nexit - exit")
while not itstime:
    gender = input(">: ").lower()

    if gender == "m":
        result = " ".join((choice(names.male_firstnames), choice(names.lastnames)))
    elif gender == "f":
        result = " ".join((choice(names.female_firstnames), choice(names.lastnames)))

    elif gender == 'exit':
        result = "Shutdown project..."
        itstime = True

    else:
        result = "please specify gender"
    print(result)
