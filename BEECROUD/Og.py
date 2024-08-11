while True:
    mao_L, mao_R = input().split()
    mao_L = int(mao_L)
    mao_R = int(mao_R)

    if mao_L == 0 and mao_R == 0:
        break

    print(mao_L + mao_R)