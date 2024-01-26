p1_age, p1_gen = map(str, input().split())
p2_age, p2_gen = map(str, input().split())

if (int(p1_age)<19 and p1_gen == 'W') or (int(p2_age)<19 and p2_gen == 'W') :
    print(0)

else :
    print(1)