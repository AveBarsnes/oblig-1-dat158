def lcs(X, Y):
    if len(X) == 0 or len(Y) == 0:
        return 0

    if X[-1] == Y[-1]:
        return 1 + lcs(X[:-1], Y[:-1])

    else:
        return max(
            lcs(X[:-1], Y),
            lcs(X, Y[:-1])
        )


X = "babbabab"
Y = "bbabbaaab"

print(lcs(X, Y))