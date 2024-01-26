mid_score, fin_score = map(int, input().split())

if mid_score >= 90 :
    if fin_score >= 95 :
        print('100000')

    elif fin_score >= 90 :
        print('50000')

    else :
        print(0)

else :
    print(0)