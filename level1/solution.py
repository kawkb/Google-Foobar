def solution(x, y):
    if len(y) > len(x):
        for i in y:
            if i not in x:
                return i
    elif len(x) > len(y):
        for i in x:
            if i not in y:
                return i
