from trans import *

def main():
    first = input("Enter your full name: ")
    names = first.split()
    customer = Customer(names[0], names[1], '256-349-8162')
    print(customer)


main()