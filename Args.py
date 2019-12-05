# args

def test(a, b):
    print(a + b)


def add(y, *firstDic):
    if y == 1:
        test(*firstDic)


print(add(1, 10, 11))

#**warg

def test1(a, b):
    print(a + b)


def add1(y, **firstDic):
    if y == 1:
        test1(**firstDic)


print(f"** here is wargs: {add1(1, a= 2, b=20)} " )





