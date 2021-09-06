def diffBetweenTwoStrings(source, target):
    """
    @param source: str
    @param target: str
    @return: str[]
    """
    sourceLen = len(source)
    targetLen = len(target)

    dp = [[0 for _ in range(targetLen+1)] for _ in range(sourceLen+1)]

    for i in range(targetLen+1):
        dp[0][i] = i

    for j in range(sourceLen+1):
        dp[j][0] = j

    # print("initial DP")
    # print(dp)

    for i in range(1, sourceLen+1):
        for j in range(1, targetLen+1):
            if source[i-1] == target[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                # dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1])

    # print("DP after for loop")
    # print(dp)

    ans = []
    i = sourceLen
    j = targetLen
    while i > 0 and j > 0:
        if source[i-1] == target[j-1]:
            ans.append(source[i-1])
            i -= 1
            j -= 1
        else:
            if dp[i][j-1] <= dp[i-1][j]:
                ans.append('+' + target[j-1])
                j -= 1
            else:
                ans.append('-' + source[i-1])
                i -= 1

    # while j < targetLen:
    #     ans.append('+' + target[j])
    #     j += 1

    # return " ".join(ans)
    return ans[::-1]


source = "ABCDEFG"
target = "ABDFFGH"

print(diffBetweenTwoStrings(source, target))
