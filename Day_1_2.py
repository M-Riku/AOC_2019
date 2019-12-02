with open('input.txt', 'r') as f:
    nums = f.readlines()

sum = 0


for s in nums:
    num = int(s)
    num = num // 3 - 2
    tmp = 0
    while num > 0:
        tmp += num
        num = num // 3 - 2
    sum += tmp
print(sum)
