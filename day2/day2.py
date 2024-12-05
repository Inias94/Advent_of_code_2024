def is_safe(line):
    increasing = True
    for i in range(len(line) - 1):
        deviation = 0
        diff = line[i + 1] - line[i]
        if not (1 <= diff <= 3):
            increasing = False
            break

    decreasing = True
    for i in range(len(line) - 1):
        diff = line[i] - line[i + 1]
        if not (1 <= diff <= 3):
            decreasing = False
            break

    return increasing or decreasing

def is_safe_part_2(line):
    if is_safe(line):
        return True

    for i in range(len(line)):
        alterd_report = line[:i] + line[i+1:]
        if is_safe(alterd_report):
            return True
    return False

safe = 0

with open("data.txt", "r") as file:
    for line in file:
        numbers = list(map(int, line.split()))

        if is_safe_part_2(numbers): # line as argument for part1
            safe += 1

print(safe)