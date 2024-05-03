def check_license(register, user):
    if user in register.keys():
        return True
    else:
        return False


def add_license(register, user, license):
    register[user] = license
    return register


def delete_license(register, user):
    del register[user]
    return register


def print_registered_users(register):
    for username, license_plate_number in register.items():
        print(f"{username} => {license_plate_number}")


def main():
    number = int(input())
    license_register = {}

    for _ in range(number):
        command = input().split()
        action = command[0]
        if action == 'register':
            username = command[1]
            license_plate_number = command[2]
            if check_license(license_register, username):
                print(f"ERROR: already registered with plate number {license_register[username]}")
            else:
                add_license(license_register, username, license_plate_number)
                print(f"{username} registered {license_plate_number} successfully")
        elif action == 'unregister':
            username = command[1]
            if check_license(license_register, username):
                delete_license(license_register, username)
                print(f"{username} unregistered successfully")
            else:
                print(f"ERROR: user {username} not found")

    print_registered_users(license_register)


if __name__ == "__main__":
    main()