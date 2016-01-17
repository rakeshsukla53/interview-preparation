def minCost(costs):
    size = len(costs)
    if size == 0:
        return 0

    pre = costs[0][:]
    now = [0]*3

    for i in xrange(size-1):
        now[0] = min(pre[1], pre[2]) + costs[i+1][0]
        now[1] = min(pre[0], pre[2]) + costs[i+1][1]
        now[2] = min(pre[0], pre[1]) + costs[i+1][2]
        pre[:] = now[:]

    return min(pre)

costs = [[1, 4, 2], [0, 15, 18], [1, 250, 100], [100, 19, 20]]

print minCost(costs)
