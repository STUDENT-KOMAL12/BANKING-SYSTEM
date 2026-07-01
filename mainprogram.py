from bankingsystem import BankingSystem
bs = BankingSystem()

while True:

    print("========BANKING SYSTEM=========")
    print("1. create account.")
    print("2. display account.")
    print("3. search account.")
    print("4. deposit money.")
    print("5. withdraw money.")
    print("6. delete account.")
    print("7. exit.")

    choice = input("enter your choice:")

    if choice == "1":
        bs.create_account()

    elif choice == "2":
        bs.display_account()

    elif choice == "3":
        bs.search_account()

    elif choice == "4":
        bs.deposit_money()

    elif choice == "5":
        bs.withdraw_money()

    elif choice == "6":
        bs.delete_account()

    elif choice == "7":
        print("Thank you")
        break

    else:
        print("invalid choice, please try again.")
                                