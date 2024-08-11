def maximo(n , k, j):
    if n >= k and n >= j:
        return n
    elif k >= n and k >= j:
        return k
    else:
        return j