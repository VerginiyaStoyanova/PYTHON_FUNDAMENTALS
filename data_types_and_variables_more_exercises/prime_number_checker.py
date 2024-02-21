number = int(input())
is_prime = True

if number <= 1:
    is_prime = False
else:
    for num in range(2, int(number**0.5) + 1):
        if number % num == 0:
            is_prime = False
            break

if is_prime:
    print(True)
else:
    print(False)