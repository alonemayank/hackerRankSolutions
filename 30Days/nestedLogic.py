d,m,y = map(int, input().split())
D,M,Y = map(int, input().split())

if y<Y:
    print(0)
elif y>Y:
    print(10000)
elif m>M:
        print((m-M)*500)
elif d>D:
        print((d-D)*15)
else:
    print(0)