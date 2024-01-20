"""
Use this file to provide your solutions for exercise 1-1 c.
"""
def levenshtein_distance(s1: str, s2: str) -> int:
    n = len(s1)+1 # number of rows in distance matrix
    m = len(s2)+1 # number of cols in distance matrix
    d = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(1,n):
        d[i][0] = i
    for j in range(1,m):
        d[0][j] = j
    for i in range(1,n):
        for j in range(1,m):
            if s1[i-1] == s2[j-1]:
                d[i][j] = d[i-1][j-1]
            else:
                d[i][j] = min(d[i-1][j],d[i][j-1],d[i-1][j-1]) + 1
    return d[-1][-1]