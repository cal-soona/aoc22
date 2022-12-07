with open('input') as input:
    lines = input.readlines()

def letter_val(c):
    val = ord(i.swapcase()) - 64
    if val > 27:
        val -= 6
    return val

total = 0

for line in lines:
    l = line.strip()
    comp1, comp2 = [*l[:len(l)//2]], [*l[len(l)//2:]]
    i = list(set(comp1).intersection(comp2))[0]
    total += letter_val(i)

print(total)
    
