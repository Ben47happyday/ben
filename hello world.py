# args

def add(*dateRage):
    print(*dateRage)
    result = 0
    for item in dateRage:
        result += item
    return result


print(add(1, 2, 3))
