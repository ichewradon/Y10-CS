import time

logged_in = False
admin = False
login_attempts = 0

users = [["admin", "admin123", True],
         ["customer", "customer123", False]]

CINEMA_NAME = "Mega-Plex"

films = [
    {"name": "A Minecraft Movie", "price": 8, "age": "PG"},
    {"name": "Spiderman", "price": 6, "age": "12"},
    {"name": "Super Mario Galaxy", "price": 10, "age": "U"}
]

snacks = {
    "Popcorn": 3,
    "Drink": 2,
    "Nachos": 4,
    "Hot-Dog": 6
}

while login_attempts < 3 and not logged_in:
    login_user = input("Enter your username: ")
    time.sleep(1)
    login_pass = input("Enter your password: ")

    for user in users:
        if login_user == user[0] and login_pass == user[1]:
            admin = user[2]
            logged_in = True
            break

    if not logged_in:
        login_attempts += 1
        print(f"Incorrect username or password. {login_attempts}/3 attempts used.")

if not logged_in:
    print("Too many failed attempts. Access denied.")
else:
    if admin:
        while True:
            print("\nADMIN MENU")
            print("1 - View films")
            print("2 - Add film")
            print("3 - Remove film")
            print("4 - Change film price")
            print("5 - View snacks")
            print("6 - Change snack price")
            print("7 - Exit")

            choice = input("Select option: ")

            if choice == "1":
                print()
                for film in films:
                    print(f"{film['name']} | £{film['price']} | {film['age']}")

            elif choice == "2":
                print()
                name = input("Film name: ")
                price = int(input("Price: "))
                age = input("Age rating: ")

                films.append({
                    "name": name,
                    "price": price,
                    "age": age
                })

                print("Film added")

            elif choice == "3":
                print()
                for i, film in enumerate(films):
                    print(i + 1, film["name"])

                pick = int(input("Select film to remove: ")) - 1

                if 0 <= pick < len(films):
                    films.pop(pick)
                    print("Film removed")
                else:
                    print("Invalid selection")

            elif choice == "4":
                print()
                for i, film in enumerate(films):
                    print(i + 1, film["name"], "£", film["price"])

                pick = int(input("Select film: ")) - 1
                new_price = int(input("New price: "))

                films[pick]["price"] = new_price

                print("Price updated")

            elif choice == "5":
                print()
                for item in snacks:
                    print(item, "£", snacks[item])

            elif choice == "6":
                print()
                for i, item in enumerate(snacks):
                    print(i + 1, item, "£", snacks[item])

                pick = int(input("Select snack: ")) - 1
                snack_name = list(snacks.keys())[pick]

                new_price = int(input("Enter new price: "))
                snacks[snack_name] = new_price

                print(snack_name, "price updated")

            elif choice == "7":
                print("Exiting admin menu...")
                break

            else:
                print("Invalid option")

    else:
        print("\nWelcome Customer")

        while True:
            print("\nCUSTOMER MENU")
            print("1. View films")
            print("2. Book tickets")
            print("3. Exit")

            choice = input("Select option: ")

            if choice == "1":
                print()
                for i, film in enumerate(films):
                    print(i + 1, film["name"], "£", film["price"], film["age"])

            elif choice == "2":
                print()
                for i, film in enumerate(films):
                    print(i + 1, film["name"], "£", film["price"], film["age"])

                pick = int(input("Choose film: ")) - 1
                selected = films[pick]

                age = int(input("Enter your age: "))

                if selected["age"] == "12" and age < 12:
                    print("You are too young for this film")
                    continue

                tickets = int(input("How many tickets? "))
                points = int(input("Loyalty points: "))

                total = tickets * selected["price"]
                total -= points // 100

                snack_total = 0
                more = "yes"

                while more == "yes":
                    print("SNACK MENU")

                    for item in snacks:
                        print(item, "£", snacks[item])

                    snack = input("Choose snack: ")

                    if snack in snacks:
                        snack_total += snacks[snack]
                        print(snack, "added")

                    more = input("Add more snacks? (yes/no): ")

                final_total = total + snack_total

                print("\n--- RECEIPT ---")
                print("Film:", selected["name"])
                print("Tickets:", tickets)
                print("Ticket cost: £", total)
                print("Snacks: £", snack_total)
                print("FINAL TOTAL: £", final_total)

            elif choice == "3":
                print("Logging Out")
                break

            else:
                print("Invalid option")