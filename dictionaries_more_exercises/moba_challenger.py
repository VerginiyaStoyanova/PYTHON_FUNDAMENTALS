players_pool = {}

while True:
    command = input()

    if command == "Season end":
        break

    if '->' in command:
        player, position, skill = command.split(' -> ')
        skill = int(skill)

        if player in players_pool:
            if position in players_pool[player]:
                players_pool[player][position] = max(players_pool[player][position], skill)
            else:
                players_pool[player][position] = skill
        else:
            players_pool[player] = {position: skill}

    elif ' vs ' in command:
        player_one, player_two = command.split(' vs ')
        if player_one in players_pool.keys() and player_two in players_pool.keys():
            for position in players_pool[player_one].keys():
                if position in players_pool[player_two].keys():
                    skill_one = sum(players_pool[player_one].values())
                    skill_two = sum(players_pool[player_two].values())
                    if skill_one > skill_two:
                        del players_pool[player_two]
                    elif skill_one < skill_two:
                        del players_pool[player_one]
                    break

player_points = [[player, sum(players_pool[player].values())] for player in players_pool.keys()]
player_ranking = [rank for rank in sorted(player_points, key=lambda item: (-item[1], item[0]))]

for rank in player_ranking:
    player, skill = rank
    print(f"{player}: {skill} skill")
    position_ranking = [rank for rank in sorted(players_pool[player].items(), key=lambda item: (-item[1], item[0]))]
    output = [f'- {position} <::> {skill}' for position, skill in position_ranking]
    print(*output, sep='\n')