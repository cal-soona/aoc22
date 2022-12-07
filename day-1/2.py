with open('input') as input:
    lines = input.readlines()

totals = []
current = 0
for line in lines:
    if line.strip().isdigit():
        current += int(line.strip())
    else:
        totals.append(current)
        current = 0

totals.append(current)
totals.sort(reverse=True)

print(totals[:3])
print(sum(totals[:3]))



