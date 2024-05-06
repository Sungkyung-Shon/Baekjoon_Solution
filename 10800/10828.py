import sys

stack = []

x = int(sys.stdin.readline())
for i in range(x):
    y = sys.stdin.readline().split()
    if y[0] == "push":
        stack.append(y[1])
    
    elif y[0] == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())

    elif y[0] =="size":
        print(len(stack))

    elif y[0] == "empty":
        if len(stack) != 0:
            print(0)
        else:
            print(1)

    elif y[0] == "top":
        if len(stack) != 0:
            print(stack[-1])
        else:
            print(-1)

 





