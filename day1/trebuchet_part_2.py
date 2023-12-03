with open('input.txt', 'r') as input:
    calibration_values = input.readlines()

alpha_digits = {
                "one": "1",
                "two": "2",
                "three": "3",
                "four": "4",
                "five": "5",
                "six": "6",
                "seven": "7",
                "eight": "8",
                "nine": "9"
                }

total = 0
for line in calibration_values:
    digits = []
    for i in range(len(line)):
        if line[i].isdigit():
            digits.append(line[i])
        else:
            for key in alpha_digits.keys():
                if key in line[i:i+5] and key[0] == line[i]:
                    digits.append(alpha_digits[key])
    total += int("".join([digits[0], digits[-1]]))

print(total)