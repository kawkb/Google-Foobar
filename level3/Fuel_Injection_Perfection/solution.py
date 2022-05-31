def solution(n):
    num = int(n)
    i = 0
    while(num != 1):
        if num == 1:
            return i
        elif num % 2 == 0:
            num = num // 2
        else:
            if ( ((num - 1) % 2 == 0 and ((num - 1) // 2) % 2 == 0) or num - 1 == 2):
                num -= 1
            elif ( (num + 1) % 2 == 0 and ((num + 1) // 2) % 2 == 0):
                num += 1
            else:
                num -= 1
        i += 1
    return i