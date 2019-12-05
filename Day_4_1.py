import collections
start = 134792
end = 675810


def increasing(x): return x == ''.join(sorted(x))


def grouped(x): return max(collections.Counter(x).values()) > 1


def valid(x): return increasing(x) and grouped(x)


ran = range(134792, 675810)
candidates = sum(1 for pas in ran if valid(str(pas)))
print(candidates)
