targets = input().split(' ')

shot_targets = 0
while True:
    command = input()

    if command == "End":
        print(f"Shot targets: {shot_targets} -> {' '.join(str(x) for x in targets)}")
        break

    index = int(command)
    if 0 <= int(index) < len(targets):
        value = int(targets[index])
        if targets[index] != "-1":
            targets[index] = "-1"
            shot_targets += 1
            for num in targets:
                if int(num) <= value and int(num) != -1:
                    increase = str(int(num) + value)
                    targets = [item.replace(num, increase) for item in targets]
                elif int(num) > value and int(num) != -1:
                    reduce = str(int(num) - value)
                    targets = [item.replace(num, reduce) for item in targets]
