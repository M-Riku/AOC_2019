with open('input.txt', 'r') as f:
    intcode = f.readline()

intcode = intcode.split(',')
intcode = [int(x) for x in intcode]

for nonu in range(100):
    for verb in range(100):
        ic = intcode.copy()
        ic[1] = nonu
        ic[2] = verb
        i = 0
        while i < len(ic):
            if ic[i] == 1:
                ic[ic[i+3]] = ic[ic[i+1]] + \
                    ic[ic[i+2]]
                i += 4
            elif ic[i] == 2:
                ic[ic[i+3]] = ic[ic[i+1]] * \
                    ic[ic[i+2]]
                i += 4
            elif ic[i] == 99:
                break
            else:
                i += 1

        if ic[0] == 19690720:
            print(100*nonu + verb)
            break
    if ic[0] == 19690720:
        break
