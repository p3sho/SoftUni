num = int(input())

matrix = [[int(el) for el in input().split(', ')] for _ in range(num)]
primary = [matrix[r][r] for r in range(num)]
secondary = [matrix[r][num - r - 1] for r in range(num)]

print(f'Primary diagonal: {", ".join(str(x) for x in primary)}. Sum: {sum(primary)}')
print(f'Secondary diagonal: {", ".join(str(x) for x in secondary)}. Sum: {sum(secondary)}')