import numpy as np
import fractions
def    solution(pegs):
    tmpmat = []
    for i in range(len(pegs)):
        tmp = []
        for j in range(len(pegs)):
            if (i == len(pegs) - 1):
                if (j == 0):
                    tmp.append(1)
                elif (j == len(pegs) - 1):
                    tmp.append(-2)
                else:
                    tmp.append(0)
            else:
                if (i == j or j == i + 1):
                    tmp.append(1)
                else:
                    tmp.append(0)
        tmpmat.append(tmp)
    mat = np.array(tmpmat)
    tmpmat2 = []
    for i in range(len(pegs) - 1):
        tmpmat2.append(pegs[i + 1] - pegs[i])
    tmpmat2.append(0)
    mat2 = np.array(tmpmat2)
    solutio = np.linalg.solve(mat, mat2)
    preret = fractions.Fraction(solutio[0]).limit_denominator()
    ret = [preret.numerator, preret.denominator]
    for i in range(len(solutio)):
        if (solutio[i] < 1):
            ret = [-1, -1]
    return ret