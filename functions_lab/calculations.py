def calculations(num1, num2, operator):
    if operator == 'multiply':
        return num1 * num2
    elif operator == 'divide':
        if num2 != 0:
            return num1 / num2
        else:
            return 'Error: Division by zero!'
    elif operator == 'add':
        return num1 + num2
    elif operator == 'subtract':
        return num1 - num2


operator = input()
num1 = int(input())
num2 = int(input())

result = calculations(num1, num2, operator)
print(f'{result:.0f}')
