command = input()
voldemort = False

while command != "Welcome!":
    name = command
    if name == "Voldemort":
        print("You must not speak of that name!")
        voldemort = True
        break
    if len(name) < 5:
        print(f"{name} goes to Gryffindor.")
    elif len(name) == 5:
        print(f"{name} goes to Slytherin.")
    elif len(name) == 6:
        print(f"{name} goes to Ravenclaw.")
    else:
        print(f"{name} goes to Hufflepuff.")

    command = input()

if not voldemort:
    print("Welcome to Hogwarts.")