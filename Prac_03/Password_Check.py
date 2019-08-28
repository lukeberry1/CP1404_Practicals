MINIMUM_LENGTH = 5


def main():
    password = get_password()

    print_asterisks(password)


def print_asterisks(password):
    print("*" * len(password))


def get_password():
    password = input("Enter a password of at least {} characters: ".format(MINIMUM_LENGTH))
    while len(password) < MINIMUM_LENGTH:
        password = input("Enter a password of at least {} characters: ".format(MINIMUM_LENGTH))
    return password


main()
