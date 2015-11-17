
A, B, N = map(int, raw_input().strip().split())

C = 0

for i in range(N - 2):
    C = pow(B, 2) + A
    A = B
    B = C

print C







