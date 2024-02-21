employee_one = int(input())
employee_two = int(input())
employee_three = int(input())
students_count = int(input())

all_employees_help = employee_one + employee_two + employee_three
hours = 0

while students_count != 0 and students_count > 0:
    students_count -= all_employees_help
    hours += 1
    if hours % 4 == 0:
        hours += 1
        continue

print(f"Time needed: {hours}h.")
