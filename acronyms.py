def find_acronym():
    look_up = input("What software acronym would you like to look up?\n")

    found = False

    try:
        with open("acronyms.txt") as file:
            for line in file:
                if look_up in line: # Substring, very good and simple
                    print(line)
                    found = True
                    break
    # except FileNotFoundError as e:
    except FileNotFoundError:
        print("File not found")
        return

    if not found:
        print("The acronym does not exist")

def add_acronym():
    acronym = input("What acronym do you want to add?\n")
    definition = input("What is the definition?\n")
    with open("acronyms.txt", "a") as file:
        file.write(f"{acronym} - {definition}\n")

def main():
    choice = input("Do you want to find(F) or add(A) and acronym?\n")
    if choice == "F":
        find_acronym()
    elif choice == "A":
        add_acronym()

main()