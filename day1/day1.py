with open("input.txt", "r") as file:
    lines = file.read().splitlines()

dial = 50
cont = 0
for line in lines:
    rotation_direction = line[0].lower()
    moves = int(line[1:])
    if rotation_direction == 'l':
        dial -= moves
    if rotation_direction == 'r':
        dial += moves
    dial %= 100
    if dial == 0:
        cont += 1

print(cont)
