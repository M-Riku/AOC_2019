with open('input.txt', 'r') as f:
    intcode = f.readline()

intcode = intcode.split(',')
intcode = [int(x) for x in intcode]
intcode[1] = 12
intcode[2] = 2

i = 0
while i < len(intcode):
    if intcode[i] == 1:
        intcode[intcode[i+3]] = intcode[intcode[i+1]] + intcode[intcode[i+2]]
        i += 4
    elif intcode[i] == 2:
        intcode[intcode[i+3]] = intcode[intcode[i+1]] * intcode[intcode[i+2]]
        i += 4
    elif intcode[i] == 99:
        break
    else:
        i += 1

resutl = str(intcode[0])
print(resutl)
