from trans import Customer


def main():
    first = input("Enter your full name: ")
    names = first.split()
    customer = Customer(names[0], names[1], "256-555-5555")
    print(customer)


main()
