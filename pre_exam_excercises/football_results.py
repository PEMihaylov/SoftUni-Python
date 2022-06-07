
games_won = 0
games_lost = 0
games_draw = 0

for game in range(3):
    game_result = input()
    home_score = int(game_result[0])
    away_score = int(game_result[2])

    if home_score > away_score:
        games_won += 1
    elif home_score == away_score:
        games_draw += 1
    elif home_score < away_score:
        games_lost += 1

print(f"Team won {games_won} games.")
print(f"Team lost {games_lost} games.")
print(f"Drawn games: {games_draw}")
