from collections import deque
eggs = deque(map(int, input().split(", ")))
papers = input().split(", ")

boxes = 0
while eggs and papers:
    if eggs[0] <= 0:
        eggs.popleft()
    elif eggs[0] == 13:
        eggs.popleft()
        papers[0], papers[-1] = papers[-1], papers[0]
    elif eggs[0] + int(papers[-1]) <= 50:
        eggs.popleft()
        papers.pop()
        boxes += 1
    elif eggs[0] + int(papers[-1]) > 50:
        eggs.popleft()
        papers.pop()


if boxes:
    print(f"Great! You filled {boxes} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")
if eggs:
   print(f"Eggs left: {', '.join(str(egg) for egg in eggs)}")
if papers:
    print(f"Pieces of paper left: {', '.join(papers)}")
