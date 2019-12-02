with open('input.txt', 'r') as f:
    nums = f.readlines()

sum = 0
for s in nums:
    num = int(s)
    tmp = num // 3 - 2
    sum += tmp
print(sum)
