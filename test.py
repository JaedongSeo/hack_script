box = []

for i in range(10):
    row = list(map(int, input().split()))
    box.append(row)

x = 1
y = 1


while box[x][y] != 1 and x < 10 and y < 10:

    if box[x][y] == 2:
        box[x][y] = 9
        break
    elif box[x][y]==0:
        box[x][y]=9

    
    if box[x][y + 1] != 1:
        y += 1
    elif box[x + 1][y] != 1:
        x += 1
    else:
        break
    

for i in range(10):
    for j in range(10):
        print(box[i][j], end=" ")
    print()
