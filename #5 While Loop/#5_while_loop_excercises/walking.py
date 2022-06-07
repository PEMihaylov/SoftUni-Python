input_line = input()
total_steps = 0

while input_line != "Going home":
    steps = int(input_line)
    total_steps += steps
    if total_steps >= 10000:
        break

    input_line = input()

if input_line == "Going home":
    steps_home = int(input())
    total_steps += steps_home

step_difference = abs(10000 - total_steps)

if total_steps >= 10000:
    print(f"Goal reached! Good job!")
    print(f"{step_difference} steps over the goal!")
else:
    print(f"{step_difference} more steps to reach goal.")