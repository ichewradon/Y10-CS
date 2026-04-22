import time

logged_in = False
admin = False
login_attempts = 0

users = [{"user": "admin", "password": "admin123", "admin": True, "points": float('inf')},
         {"user": "james", "password": "james123", "admin": False, "points": 800},
         {"user": "gethin", "password": "gethin123", "admin": False, "points": 100}]


CINEMA_NAME = "Mega-Plex"

films = [
    {"name": "A Minecraft Movie", "price": 8, "age": "PG", "seats": 50},
    {"name": "Spiderman", "price": 6, "age": "12", "seats": 50},
    {"name": "Super Mario Galaxy", "price": 10, "age": "U", "seats": 50}
]

snacks = {
    "Popcorn": {"price": 3, "quantity": "500"},
    "Drink": {"price": 2, "quantity": "200"},
    "Nachos": {"price": 4, "quantity": "100"},
    "Hot-Dog": {"price": 3, "quantity": "50"}
}

while login_attempts < 3 and not logged_in:
    login_user = input("Enter your username: ")
    time.sleep(1)
    login_pass = input("Enter your password: ")

    for user in users:
        if login_user == user["user"] and login_pass == user["password"]:
            admin = user["admin"]
            logged_in = True
            name = user["user"].title()
            points = user["points"]
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
                    print(f"{film['name']} | £{film['price']} | {film['age']} | {film['seats']} seats left")

            elif choice == "2":
                print()
                name = input("Film name: ")
                price = int(input("Price: "))
                age = input("Age rating: ")
                seats = int(input("Number of seats: "))


                films.append({
                    "name": name,
                    "price": price,
                    "age": age,
                    "seats": seats
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
                for name, snack in snacks.items():
                    print(f"{name} | £{snack['price']} | {snack['quantity']} left")

            elif choice == "6":
                print()
                snack_list = list(snacks.keys())
                for i, name in enumerate(snack_list):
                    print(i + 1, name, "£", snacks[name]["price"])

                pick = int(input("Select snack: ")) - 1

                if 0 <= pick < len(snack_list):
                    snack_name = snack_list[pick]
                    new_price = int(input("Enter new price: "))
                    snacks[snack_name]["price"] = new_price
                    print(snack_name, "price updated")
                else:
                    print("Invalid selection")

            elif choice == "7":
                print("Exiting admin menu...")
                break

            else:
                print("Invalid option")

    else:
        print(f"\nWelcome {name}")

        while True:
            print("\nCUSTOMER MENU")
            print("1. View films")
            print("2. Book tickets")
            print("3. Exit")

            choice = input("Select option: ")

            if choice == "1":
                print()
                for film in films:
                    print(f"{film['name']} | £{film['price']} | {film['age']} | {film['seats']} seats left")

            elif choice == "2":
                print()
                for i, film in enumerate(films):
                    print(f" {i + 1} - {film['name']} | £{film['price']} | {film['age']} | {film['seats']} seats left")

                pick = int(input("Choose film: ")) - 1
                selected = films[pick]

                age = int(input("Enter your age: "))

                if selected["age"] == "12" and age < 12:
                    print("You are too young for this film")

                tickets = int(input("How many tickets? "))

                if tickets <= selected["seats"]:
                    total = tickets * selected["price"]
                    selected["seats"] -= tickets
                    total -= points // 100

                    snack_total = 0
                    more = "yes"

                    while more == "yes":
                        print("SNACK MENU")

                        for i, (name, snack) in enumerate(snacks.items()):
                            print(i + 1, name, "£", snack["price"])

                        snack = input("Choose snack: ")

                        if snack in snacks:
                            snack_total += snacks[snack]["price"]
                            print(snack, "added")

                        more = input("Add more snacks? (yes/no): ")

                    final_total = total + snack_total

                    print("\n--- RECEIPT ---")
                    print("Film:", selected["name"])
                    print("Tickets:", tickets)
                    print("Ticket cost: £", total)
                    print("Snacks: £", snack_total)
                    print("FINAL TOTAL: £", final_total)
                
                else:
                    print("Not enough seats available")

            elif choice == "3":
                print("Logging Out")
                break

            else:
                print("Invalid option")