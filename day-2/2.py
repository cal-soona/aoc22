with open('input') as input:
    lines = input.readlines()

score = {
        "A X": 3 + 0,
        "A Y": 1 + 3,
        "A Z": 2 + 6,
        "B X": 1 + 0,
        "B Y": 2 + 3,
        "B Z": 3 + 6,
        "C X": 2 + 0,
        "C Y": 3 + 3,
        "C Z": 1 + 6
        }

total_score = 0
for line in lines:
    total_score += score[line.strip()]
print(total_score)

