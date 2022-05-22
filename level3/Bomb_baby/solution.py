def getGen(x, y, gen):
    if x == y:
        return str(gen) if (x, y)==(1, 1) else 'impossible'
    if y > x:
        gen += (y-x)//x + ((y-x) % x > 0)
        return getGen(x, y - ((y-x)//x + ((y-x) % x > 0)) * x, gen)
    else:
        gen += (x-y)//y + ((x-y) % y > 0)
        return getGen(x - ((x-y)//y + ((x-y) % y > 0)) * y, y, gen)

def solution(x, y):
    return getGen(int(x), int(y), 0)