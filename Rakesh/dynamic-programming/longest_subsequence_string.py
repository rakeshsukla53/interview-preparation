

# size of the matrix here will be length(string1) + 1 * length(string2) + 1

columnString = list(raw_input().strip())
rowString = list(raw_input().strip())

dynamicMatrix = [[0 for item_idx in range(len(columnString)+1)] for row_idx in range(len(rowString) + 1)]

for i in range(len(rowString)):

    for j in range(len(columnString)):

        if rowString[i] == columnString[j]:

            dynamicMatrix[i + 1][j + 1] = dynamicMatrix[i][j] + 1

        else:
            dynamicMatrix[i + 1][j + 1] = max(dynamicMatrix[i+1][j], dynamicMatrix[i][j+1])

print dynamicMatrix[len(rowString)][len(columnString)]
