upper_limit_first = int(input())
upper_limit_second = int(input())
upper_limit_third = int(input())
is_prime = True

for x in range(2, upper_limit_first + 1):
    if x % 2 == 0:
        for y in range(2, upper_limit_second + 1):
            if y == 2:
                for z in range(1, upper_limit_third + 1):
                    if z % 2 == 0:
                        print(x, y, z)
            else:
                for i in range(2, y):
                    if y % i == 0:
                        is_prime = False
                        break
                if is_prime:
                    for z in range(2, upper_limit_third + 1):
                        if z % 2 == 0:
                            print(x, y, z)
            is_prime = True