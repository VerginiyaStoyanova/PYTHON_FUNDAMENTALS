contests = {}

command = input()
while command != "end of contests":
    contest, password = command.split(':')
    if contest not in contests:
        contests[contest] = password

    command = input()

candidates = {}

command = input()
while command != "end of submissions":
    command = command.split('=>')
    contest = command[0]
    password = command[1]
    username = command[2]
    points = int(command[3])
    if contest in contests and password == contests[contest]:
        if username not in candidates:
            candidates[username] = {contest: points}
        else:
            if contest in candidates[username]:
                candidates[username][contest] = max(candidates[username][contest], points)
            else:
                candidates[username][contest] = points

    command = input()

sorted_candidates = {}
for key, value in candidates.items():
    candidates[key] = dict(sorted(value.items(), key=lambda x: x[1], reverse=True))
    sorted_candidates = dict(sorted(candidates.items()))
print(sorted_candidates)

max_points = 0
max_user = ""
for key, value in candidates.items():
    sum_value = sum(candidates[key].values())
    if sum_value > max_points:
        max_points = sum_value
        max_user = key

print(f"Best candidate is {max_user} with total {max_points} points.")
print("Ranking:")
for key, value in sorted_candidates.items():
    print(f"{key}")
    for contest, points in value.items():
        print(f"#  {contest} -> {points}")