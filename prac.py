i = 0
check = "Up"
while True:
    if i == 10:
        check = "Down"
    elif i == 0:
        check = "Up"
    if check == "Up":
        i += 1
    if check == "Down":
        i = i - 1
    print(i)