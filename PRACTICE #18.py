def shop():
    jacket_price = 1000
    t_shirt_price = 300
    pants_price = 500
    socks_price = 100
    hankerchief_price = 50
    cap_price = 150

    print("         Welcome to our Lazapee!         ")
    print("=========================================")
    print("Would you like to [1] buy or [2] leave?")
    buy = input("Press number [1] to buy, [2] to leave: ")

    if buy == '1':
        while buy == '1':
            total = 0
            print("=======================================")
            print("         Here are our products:         ")
            print("[1] Jacket ............ ₱", jacket_price)
            print("[2] T-shirt ........... ₱", t_shirt_price)
            print("[3] Pants ............. ₱", pants_price)
            print("=======================================")
            print("Enter the product number you want to buy: ", end='')
            product_choice = int(input())
            print("Enter the quantity you want to buy: ", end='')
            quantity = int(input())
            if product_choice == 1:
                total += jacket_price * quantity
            elif product_choice == 2:
                total += t_shirt_price * quantity
            elif product_choice == 3:
                total += pants_price * quantity
            else:
                print("Invalid product choice.")
                return

            print("Your total is: ₱", total)
            payment = float(input("Enter the amount you want to pay: ₱"))
            if payment < total:
                print("Insufficient payment. Please pay the full amount.")
                return

            change = payment - total
            print("Thank you for your purchase!")
            print("Receipt:")
            print("Total: ₱", total)
            print("Payment: ₱", payment)
            print("Change: ₱", change)
            print("=======================================")
            print("Would you like to add add-ons? : ")
            yes = int(input("Press [1] for Yes, [2] for No "))
            if yes == 1:
                add_ons_total = 0
                print("=======================================")
                print("Here are our add-ons:")
                print("[1] Socks ................ ₱", socks_price)
                print("[2] Hankerchief .......... ₱", hankerchief_price)
                print("[3] Cap .................. ₱", cap_price)
                print("=======================================")
                print("Enter the add-on number you want to buy: ", end='')
                add_on_choice = int(input())
                print("Enter the quantity of add-ons you want to buy: ", end='')
                add_on_quantity = int(input())
                if add_on_choice == 1:
                    add_ons_total += socks_price * add_on_quantity
                elif add_on_choice == 2:
                    add_ons_total += hankerchief_price * add_on_quantity
                elif add_on_choice == 3:
                    add_ons_total += cap_price * add_on_quantity
                else:
                    print("Invalid add-on choice.")
                    return
                print("Your add-ons total is: ₱", add_ons_total)
                total += add_ons_total
                change2 = payment - total
                print("Final Receipt:")
                print("Total: ₱", total)
                print("Payment: ₱", payment)
                print("Change: ₱", change2)
                print("Thank you for Buying 😃. Please Come Again!")
                break
            else:
                change2 = payment - total
                print("Final Receipt:")
                print("Total: ₱", total)
                print("Payment: ₱", payment)
                print("Change: ₱", change2)
                print("Thank you for Buying 😃. Please Come Again!")
                break

        else:
            print("Thank you for visiting our shop")

    elif buy == '2':
        print("Thank you for visiting our shop")

    else:
        print("invalid input please try again")

shop()