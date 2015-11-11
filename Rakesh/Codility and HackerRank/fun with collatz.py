
def collatz_conjecture(x, y):
    output = [x]
    for i in range(y):
       if x % 2 == 0:
         x = x / 2
       else:
         x = 3 * x + 1
       output.append(x)
    return output[-1]

user_input = map(int, raw_input().strip().split(' '))
N, K = user_input[0], user_input[1]

print collatz_conjecture(N, K)

