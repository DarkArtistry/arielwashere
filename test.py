import numpy as np;
arrayA = np.zeros ((6,6))
arrayA[0][0] = 1
arrayA[1][0] = 1

if arrayA[0,0] == arrayA[1,0]:
    print('they are the same !')