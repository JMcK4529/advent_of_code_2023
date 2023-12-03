with open('input.txt', 'r') as input:
    calibration_values = input.readlines()

calibration_ints = []
for line in calibration_values:
    ints = [char for char in line if char.isdigit()]
    calibration_ints.append(
            int(
                "".join([ints[0], ints[-1]])
                    
                )
            )

print(sum(calibration_ints))