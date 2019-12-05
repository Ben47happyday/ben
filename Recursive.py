# n! = 1 * 2 * 3 * 4 ......(N-1) * N

def MyRecursiveTest(n):

    if n == 1:
        return n
    return n * MyRecursiveTest(n-1)

print(MyRecursiveTest(10))
