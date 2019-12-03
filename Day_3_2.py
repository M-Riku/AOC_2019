with open('input.txt', 'r') as f:
    first = f.readline.split(',')
    second = f.readline.split(',')

dir_dic = {'R': [1, 0], 'L': [-1, 0], 'U': [0, -1], 'D': [0, 1]}
fir = []
start = [0, 0]
for step in first:
    dir = dir_dic[step[0]]
    dis = int(step[1:])
    for i in range(dis):
        start[0] += dir[0]
        start[1] += dir[1]
        fir.append(start.copy())

start = [0, 0]
sec = []
same_point = []
for step in second:
    dir = dir_dic[step[0]]
    dis = int(step[1:])
    for i in range(dis):
        start[0] += dir[0]
        start[1] += dir[1]
        sec.append(start.copy())
        if start in fir:
            same_point.append(start.copy())

min_dis = fir.index(same_point[0]) + sec.index(same_point[0])
for s in same_point[1:]:
    temp_dis = fir.index(s) + sec.index(s)
    if temp_dis < min_dis:
        min_dis = temp_dis
print(min_dis+2)
