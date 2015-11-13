def total_beers(N, B, M):
    total_beers_caps = N / B
    result = total_beers_caps
    if total_beers_caps < M:
        return total_beers_caps
    while total_beers_caps >= M:
        result += 1
        total_beers_caps = total_beers_caps - M + 1

    return result

n = input()
for i in range(n):
    N, B, M = map(int, raw_input().strip().split())
    print total_beers(N, B, M)

