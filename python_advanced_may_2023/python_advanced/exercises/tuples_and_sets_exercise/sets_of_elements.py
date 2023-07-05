n, m = [int(num) for num in input().split()]
n_set = set()
m_set = set()

for _ in range(n):
    num = input()
    n_set.add(num)

for _ in range(m):
    num = input()
    m_set.add(num)

print("\n".join(n_set.intersection(m_set)))