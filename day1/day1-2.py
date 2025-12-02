with open("input.txt", "r") as file:
    lines = file.read().splitlines()

dial = 50
cont = 0
for line in lines:
    rotation_direction = line[0].lower()
    moves = int(line[1:])
    old_dial = dial
    if rotation_direction == 'l':
        dial -= moves
    if rotation_direction == 'r':
        dial += moves
    ticks = abs(int(dial/100))
    if dial <= 0 and old_dial != 0:
        ticks+=1
    dial %= 100
    print(f"{dial} -> {ticks} ticks")
    cont += ticks

print(cont)
