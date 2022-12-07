with open('input') as input:
    lines = input.readlines()

best = 0
current = 0
for line in lines:
    if line.strip().isdigit():
        current += int(line.strip())
    else:
        best = max(best,current)
        current = 0
print(best)

