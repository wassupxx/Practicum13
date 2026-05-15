solutions = []

for X in range(1, 10):
    for O in range(10):
        for D in range(10):
            if len({X, O, D}) != 3:
                continue

            HOD = 100 * X + 10 * O + D
            MAT = 3 * HOD

            if MAT >= 1000 or MAT < 100:
                continue

            M = MAT // 100
            A = (MAT % 100) // 10
            T = MAT % 10

            if len({X, O, D, M, A, T}) != 6:
                continue
            if M == 0:
                continue

            solutions.append(f"{HOD}+{HOD}+{HOD}={MAT}")

solutions.sort(key=lambda s: int(s.split('+')[0]))

print("\n".join(solutions))
