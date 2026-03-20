from colorama import Fore, Back, Style
import pandas as pd


class brewbloomcafe:

    def __init__(self):

        print("\t\t\t Brew Bloom Cafe")
        print("\t\t\t Started - 2025")
        print("\t\t\t Near Akshya Patr")

        print("\n\nMENU")

        menu = ["Indian", "German", "Italian", "Korean"]

        for i in menu:
            print(i)

    # ---------- BILLING ----------
    def billing(self, food, price, color):

        df = pd.DataFrame({"Food": food, "Price": price})
        print("\nFood Menu\n")
        print(df)

        bill = []

        while True:

            try:
                b = int(input("Enter item number: "))

                if b < 0 or b >= len(food):
                    print("❌ This item is not available in the menu.")
                    continue

                q = int(input("Enter quantity: "))

                total_item = price[b] * q
                bill.append(total_item)

            except ValueError:
                print("❌ Please enter a valid number.")
                continue

            ch = input("Reorder? (yes/no): ")

            if ch.lower() == "no":
                break

        total = sum(bill)
        tax = total * 0.05
        final = total + tax

        print(color + "\n----------- BILL SUMMARY -----------")
        print("Total Amount :", total, "Rupees")
        print("Service Tax (5%) Applied")
        print("Final Amount :", final, "Rupees")
        print("------------------------------------")

        print(Style.RESET_ALL)

    # ---------- INDIAN ----------
    def indian(self):

        food = ["Pav Bhaji", "Khaman", "Masala Dosa", "Fry Idli", "Sambhar Vada"]
        price = [60, 20, 60, 30, 20]

        self.billing(food, price, Back.GREEN + Fore.WHITE + Style.BRIGHT)

    # ---------- GERMAN ----------
    def german(self):

        food = ["Bratwurst", "Schnitzel", "Pretzel", "Sauerkraut", "Kartoffelsalat"]
        price = [200, 300, 80, 150, 120]

        self.billing(food, price, Back.YELLOW + Fore.BLACK + Style.BRIGHT)

    # ---------- ITALIAN ----------
    def italian(self):

        food = ["Pizza", "Pasta", "Lasagna", "Risotto", "Tiramisu"]
        price = [250, 220, 300, 260, 180]

        self.billing(food, price, Back.RED + Fore.WHITE + Style.BRIGHT)

    # ---------- KOREAN ----------
    def korean(self):

        food = ["Kimchi", "Bibimbap", "Tteokbokki", "Bulgogi", "Japchae"]
        price = [120, 250, 180, 320, 200]

        self.billing(food, price, Back.WHITE + Fore.BLACK + Style.BRIGHT)


# -------- MAIN PROGRAM --------

obj = brewbloomcafe()

x = input("enter the type of food: ")

if x.lower() == "indian":
    obj.indian()

elif x.lower() == "german":
    obj.german()

elif x.lower() == "italian":
    obj.italian()

elif x.lower() == "korean":
    obj.korean()

else:
    print("wrong option:\n please again choose the right option:")