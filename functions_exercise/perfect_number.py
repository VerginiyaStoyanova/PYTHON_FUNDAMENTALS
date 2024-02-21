def is_perfect_number(number):
    divisors_sum = sum(divisor for divisor in range(1, number) if number % divisor == 0)

    if divisors_sum == number:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


num = int(input())
print(is_perfect_number(num))