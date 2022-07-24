import csv
import os
import matplotlib.pyplot as plt

income = 0
path = "data.csv"


def enter_data():

    if not os.path.exists("data.csv"):
        with open(path, "w") as file:
            entry = csv.writer(file)
            entry.writerow(["DATE", "LABEL", "EXPENSE"])

    date = input("ENTER THE DATE (DD/MM/YYYY): ")
    label = input("LABEL YOUR EXPENSE: ")
    expense = int(input("EXPENDITURE: "))

    with open(path, "a") as file:  # "w" will over write the file
        entry = csv.writer(file)
        entry.writerow([date, label, expense])


def add_money():
    deposit = int(input("ENTER THE DEPOSIT AMOUNT: "))
    global income
    income = income + deposit


def file_info():
    try:
        with open(path, "r") as file:
            read = csv.reader(file)
            read_list = list(read)
            total_expense = 0
            for t in read_list[1:]:
                total_expense = total_expense + int(t[2])

            balance = income - total_expense
            print(
                f"ACCOUNT BALANCE: {balance}\nTOTAL EXPENDITURE THIS MONTH: {total_expense}\n")
            percent = float(total_expense / income * 100)
            print(f"EXPENDITURE IS {percent}% OF THE INCOME\n")
    except Exception:
        print("ERROR!!!")


def graph():

    with open(path, "r") as file:

        dates = []
        expenses = []

        read = csv.reader(file)
        file_list = list(read)

        for f in file_list[1:]:
            dates.append((f[0]))
            expenses.append(int(f[2]))

            plt.style.use("fivethirtyeight")

            plt.figure(figsize=(10, 6), dpi=80)
            plt.plot(dates, expenses, marker='o', label="Expenditure")

            plt.title("---EXPENDITURE GRAPH---")
            plt.xlabel("DATE")
            plt.ylabel("EXPENDITURE")

            plt.grid(True, color='k', linestyle=':')
            plt.tight_layout()
            plt.legend()
            plt.show()


def main():

    a = 0
    while a == 0:
        choice = int(input(
            "1. ADD MONEY\t2. ENTER DATA\n3. DISPLAY \t4. GRAPHICAL REPRESENTATION\n5. EXIT\n"))
        if choice == 1:
            add_money()
        elif choice == 2:
            enter_data()
        elif choice == 3:
            file_info()
        elif choice == 4:
            graph()
        elif choice == 5:
            x = (input("DO YOU WANT TO EXIT? (Y/N): "))
            if x == "y" or x == "Y":
                a = 1
        else:
            print("PLEASE ENTER A VALID OPTION!!!")


main()
