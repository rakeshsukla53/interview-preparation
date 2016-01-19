
# method 1
block = [1, 2, 3, 4, 5, 6, 7, 8]
i = 0
result = []
while i <= len(block):
    if block[i] == 5:
        break
    result.append(block[i])
    i += 1

print result

# here if the block is callable then it will work otherwise not.

result = []
for value in iter(block, 5):
    result.append(value)

print result
