def printTest(n, k, a):
    print( str(n) + " " + str(k))
    print( " ".join(map(str, a)))

tests = 5
print(tests)
printTest(7, 6, [2, 0, -1, 1, 1, 1, 1])
printTest(4, 3, [-1, 0, 4, 2])
printTest(6, 4, [0, -1, 1, 4, 5, 6])
printTest(5, 2, [0, -1, 2, 1, 4])
printTest(3, 1, [-1, 0, 4])
