from collections import Counter

with open('data.txt') as file:
    lines = file.readlines()


# Part 1 -----------
left_list = [int(line.split()[0]) for line in lines]
right_list = [int(line.split()[1]) for line in lines]

left_list.sort()
right_list.sort()

distance = zip(left_list, right_list)
calculated_distance = sum(abs(left - right) for left, right in distance)

# print(list(distance))

print(calculated_distance)

# Part 2 ----------
amount_in_right_list = Counter(right_list)
sim_score = sum(left * amount_in_right_list[left] for left in left_list)
print(sim_score)