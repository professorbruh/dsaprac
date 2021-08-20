n = int(input("Board Size"))
k = int(input("Obstacles"))

r_q = int(input())
c_q = int(input())

obstacles = []

for _ in range(k):
    obstacles.append(list(map(int, input().rstrip().split())))

ctr = 0
for i in range(1, n):
    if i + r_q < n:
        if [i + r_q, c_q] not in obstacles:
            ctr += 1

    if i + c_q < n:
        if [r_q, i + c_q] not in obstacles:
            ctr += 1

    if r_q - i >= 0:
        if [r_q - i, c_q] not in obstacles:
            ctr += 1

    if c_q - i >= 0:
        if [r_q, c_q - i] not in obstacles:
            ctr += 1

    if i + r_q < n and i + c_q < n:
        if [i + r_q, i + c_q] not in obstacles:
            ctr += 1

    if r_q - i >= 0 and c_q - i >= 0:
        if [r_q - i, c_q - i] not in obstacles:
            ctr += 1

    if r_q - i >= 0 and c_q + i < n:
        if [r_q-i, c_q+i] not in obstacles:
            ctr += 1

    if r_q + i < n and c_q - i >= 0:
        if [r_q+i, c_q-i] not in obstacles:
            ctr += 1

print(ctr)