def robot(N):
    x, y = 0, 0
    step, count = 1, 0
    direction = 0  

    for _ in range(1, N + 1):
        if direction == 0:
            x += 1
        elif direction == 1:
            y -= 1
        elif direction == 2:
            x -= 1
        elif direction == 3:
            y += 1
            
        count += 1
        if count == step:
            count = 0
            direction = (direction + 1) % 4
            if direction == 0 or direction == 2:
                step += 1

    return x, y

N = int(input())
x, y = robot(N)
print(x, y)
        
