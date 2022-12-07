with open('input') as input:
    lines = input.readlines()

def letter_val(c):
    val = ord(i.swapcase()) - 64
    if val > 27:
        val -= 6
    return val

total = 0

for x in range(0, len(lines), 3):
    i1 = [*lines[x].strip()]
    i2 = [*lines[x+1].strip()]
    i3 = [*lines[x+2].strip()]
    i = list(set(i1).intersection(i2).intersection(i3))[0]
    total += letter_val(i)

print(total)
    
