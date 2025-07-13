# include cs50.h

def main():
    while True:
        try:
            dollars = float(input("Change owed: "))
            if dollars >= 0:
                break

        except ValueError:
            pass

    cents = round(dollars * 100)

    quarters = calculate_quarters(cents)  # Calculate how many quarters you should give customer
    cents = cents - (quarters * 25)  # Subtract the value of those quarters from cents

    dimes = calculate_dimes(cents)  # Calculate how many dimes you should give customer
    cents = cents - (dimes * 10)  # Subtract the value of those dimes from cents

    nickels = calculate_nickels(cents)  # Calculate how many nickels you should give customer
    cents = cents - (nickels * 5)  # Subtract the value of those nickels from cents

    pennies = calculate_pennies(cents)  # Calculate how many pennies you should give customer
    cents = cents - (pennies)  # Subtract the value of those pennies from cents

    total_coins = quarters + dimes + nickels + pennies

    print(f"{total_coins}")


def calculate_quarters(cents):  # quarters (25¢)

    return cents // 25  # Calculate how many quarters you should give customer


def calculate_dimes(cents):  # dimes (10¢)

    return cents // 10  # Calculate how many quarters you should give customer


def calculate_nickels(cents):  # nickels (5¢)

    return cents // 5  # Calculate how many quarters you should give customer


def calculate_pennies(cents):  # pennies (1¢)

    return cents // 1  # Calculate how many quarters you should give customer


main()
