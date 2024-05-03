judge = {}

while True:
    command = input()

    if command == "no more time":
        break
    data = command.split(' -> ')
    username = data[0]
    contest = data[1]
    points = int(data[2])
    if contest in judge:
        if username in judge[contest]:
            judge[contest][username] = max(judge[contest][username], points)
        else:
            judge[contest][username] = points
    else:
        judge[contest] = {username: points}

for key, value in judge.items():
    print(f"{key}: {len(value)} participants")
    sorted_judge = dict(sorted(value.items(), key=lambda item: (-item[1], item[0])))
    number = 1
    for kay2, value2 in sorted_judge.items():
        print(f"{number}. {kay2} <::> {value2}")
        number += 1

print("Individual standings:")

user_points = {}

for contest, users in judge.items():

    for user, points in users.items():
        if user in user_points:
            user_points[user] += int(points)
        else:
            user_points[user] = int(points)

sorted_max_points = dict(sorted(user_points.items(), key=lambda x: (-x[1], x[0])))

number = 1
for key, value in sorted_max_points.items():
    print(f"{number}. {key} -> {value}")
    number += 1