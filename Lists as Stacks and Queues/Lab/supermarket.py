from collections import deque
queue = deque()

while True:
    inline = input()
    if inline == "Paid":
        while len(queue):
            print(queue.popleft())

    elif inline == "End":
        print(f"{len(queue)} people remaining.")
        break

    else:
        queue.append(inline)


