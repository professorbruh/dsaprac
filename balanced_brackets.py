k = input()
stack = []
flag = True
for i in k:
    if i == "(" or i == "[" or i == '{':
        stack.append(i)

    if i ==")" or i=="]" or i=="}":
        try:
            stack.pop()
        except:
            flag = False
            continue

print(stack)
if flag and len(stack) == 0:
    print("balanced")
else:
    print('unbalanced')