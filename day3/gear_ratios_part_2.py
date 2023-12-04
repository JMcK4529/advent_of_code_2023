with open('input.txt', 'r') as inputs:
    inputs = inputs.readlines()


"""
Keep a list of digits that are adjacent to a symbol
Also add any digits that form an adjacent set up to length 3
"""
coordinates = []
locs = []
for row in range(1, len(inputs) - 1):
    for col in range(1, len(inputs[row]) - 1):
        if inputs[row][col].isdigit() or inputs[row][col] == ".":
            pass
        else:
            locs.append([row, col, inputs[row][col]])
            if inputs[row - 1][col - 1].isdigit() and (row - 1, col - 1) not in coordinates:
                coordinates.append((row - 1, col - 1))
                if inputs[row - 1][col - 2].isdigit() and (row - 1, col - 2) not in coordinates:
                    coordinates.append((row - 1, col - 2))
                    if inputs[row - 1][col - 3].isdigit() and (row - 1, col - 3) not in coordinates:
                        coordinates.append((row - 1, col - 3))

            if inputs[row - 1][col].isdigit() and (row - 1, col) not in coordinates:
                coordinates.append((row - 1, col))

            if inputs[row - 1][col + 1].isdigit() and (row - 1, col + 1) not in coordinates:
                coordinates.append((row - 1, col + 1))
                if inputs[row - 1][col + 2].isdigit() and (row - 1, col + 2) not in coordinates:
                    coordinates.append((row - 1, col + 2))
                    if inputs[row - 1][col + 3].isdigit() and (row - 1, col + 3) not in coordinates:
                        coordinates.append((row - 1, col + 3))

            if inputs[row + 1][col - 1].isdigit() and (row + 1, col - 1) not in coordinates:
                coordinates.append((row + 1, col - 1))
                if inputs[row + 1][col - 2].isdigit() and (row + 1, col - 2) not in coordinates:
                    coordinates.append((row + 1, col - 2))
                    if inputs[row + 1][col - 3].isdigit() and (row + 1, col - 3) not in coordinates:
                        coordinates.append((row + 1, col - 3))

            if inputs[row + 1][col].isdigit() and (row + 1, col) not in coordinates:
                coordinates.append((row + 1, col))

            if inputs[row + 1][col + 1].isdigit() and (row + 1, col + 1) not in coordinates:
                coordinates.append((row + 1, col + 1))
                if inputs[row + 1][col + 2].isdigit() and (row + 1, col + 2) not in coordinates:
                    coordinates.append((row + 1, col + 2))
                    if inputs[row + 1][col + 3].isdigit() and (row + 1, col + 3) not in coordinates:
                        coordinates.append((row + 1, col + 3))

            if inputs[row][col - 1].isdigit() and (row, col - 1) not in coordinates:
                coordinates.append((row, col - 1))
                if inputs[row][col - 2].isdigit() and (row, col - 2) not in coordinates:
                    coordinates.append((row, col - 2))
                    if inputs[row][col - 3].isdigit() and (row, col - 3) not in coordinates:
                        coordinates.append((row, col - 3))
            
            if inputs[row][col + 1].isdigit() and (row, col + 1) not in coordinates:
                coordinates.append((row, col + 1))
                if inputs[row][col + 2].isdigit() and (row, col + 2) not in coordinates:
                    coordinates.append((row, col + 2))
                    if inputs[row][col + 3].isdigit() and (row, col + 3) not in coordinates:
                        coordinates.append((row, col + 3))

coordinates.sort()

"""
Iterate through and add each part number of up to 3 digits in length
"""
total = 0
i = 0
while i < len(coordinates)-2:
    part_number = ""
    pos1 = coordinates[i][1]
    pos2 = coordinates[i+1][1]
    pos3 = coordinates[i+2][1]
    part_number += inputs[coordinates[i][0]][coordinates[i][1]]
    i += 1
    if pos2-pos1 == 1:
        part_number += inputs[coordinates[i][0]][coordinates[i][1]]
        i += 1
        if pos3-pos2 == 1:
            part_number += inputs[coordinates[i][0]][coordinates[i][1]]
            i += 1
    total += int(part_number)

"""
If there are any 2 or 1 digit part numbers left at the end, add them to the total
"""
part_number = ""
for i in range(len(coordinates)-2, len(coordinates)):
    part_number += inputs[coordinates[i][0]][coordinates[i][1]]
total += int(part_number)

print(total)