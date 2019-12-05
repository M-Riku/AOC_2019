import collections
start = 134792
end = 675810


def increasing(x): return x == ''.join(sorted(x))


def grouped(x): return 2 in collections.Counter(x).values()


def valid(x): return increasing(x) and grouped(x)


ran = range(134792, 675810)
candidates = sum(1 for pas in ran if valid(str(pas)))
print(candidates)
