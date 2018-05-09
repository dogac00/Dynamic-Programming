def lcs(X, Y, m, n):
    x_len = len(X)
    y_len = len(Y)
 
    if m == 0 or n == 0: # if both strings are empty
       return 0;
    elif X[m-1] == Y[n-1]:              # if last elements match
       return 1 + lcs(X, Y, m-1, n-1);  # find lcs without the last element plus 1 - it is the last element
    else:
       return max(lcs(X, Y, m, n-1), lcs(X, Y, m-1, n)); # max of lcs's of X and Y without the last, and
                                                         # Y and X without last

X = "AGGTAB"
Y = "GXTXAYB"
print("Length of LCS is ", lcs(X , Y, len(X), len(Y)))
