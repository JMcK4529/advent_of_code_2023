with open('input.txt', 'r') as inputs:
    game_inputs = inputs.readlines()

"""
Start by turning games and subsets into lists of rgb numbers
e.g.
[
  [
    [1, 1, 1], [2, 1, 2], [3, 3, 0]
  ],
  [
    [4, 0, 2], [0, 1, 1], [12, 7, 0]
  ]
]
This would be 2 games, each with three subsets of cubes.
The number of red cubes in the 3rd draw of the 2nd game is 12,
the number of green cubes in that draw is 7,
and the number of blue cubes is 0.
"""
games = []
for game in game_inputs:
    game = game.split(":")[-1]
    dips = []
    for dip in game.split(";"):
        dips.append(dip.strip())
    balls_list = []
    for dip in dips:
        balls = [0,0,0]
        unordered_balls = dip.split(",")
        red, green, blue = False, False, False
        for part in unordered_balls:
            if part[-3:] == "red" and not red:
                balls[0] = int(part.strip()[:-4])
                red = True
            if part[-5:] == "green" and not green:
                balls[1] = int(part.strip()[:-6])
                green = True
            if part[-4:] == "blue" and not blue:
                balls[2] = int(part.strip()[:-5])
                blue = True
        if not red:
            balls[0] = 0
        if not green:
            balls[1] = 0
        if not blue:
            balls[2] = 0
        balls_list.append(balls)
    games.append(balls_list)

total = 0
for game_number in range(len(games)):
    r, g, b = zip(*games[game_number])
    min_red = max(r)
    min_green = max(g)
    min_blue = max(b)
    power = min_red * min_green * min_blue
    total += power
print(total)