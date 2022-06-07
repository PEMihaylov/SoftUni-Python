actor_name = str(input())
academy_points = float(input())
n = int(input())

total_juries_points = 0
total_points = 0

for i in range(1, n+1):
    actor_jury = str(input())
    jury_evaluation = float(input())

    jury_points = (len(actor_jury) * jury_evaluation) / 2
    total_juries_points += jury_points
    final_points = academy_points + total_juries_points

    if final_points > 1250.5:
        break

if final_points > 1250.5:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {final_points:.1f}!")
else:
    print(f"Sorry, {actor_name} you need {(1250.5- final_points):.1f} more!")
