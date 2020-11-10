# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import sys
import random


def map_gen(x, y, density):
    m=[[0 for k in range(x)] for l in range(y)]
    print('{}.ox'.format(y))
    for i in range(int(y)):
        for j in range(int(x)):
            if (random.randint(0, int(y)) * 2) < int(density):
                #print('o', end='')
                m[i][j]= 'o'
            else:
                m[i][j] = '.'
                #print('.', end='')
        #print('', end='\n')
    return m


def printMaxSubSquare(M):
    R = len(M)  # no. of rows in M[][]
    C = len(M[0])  # no. of columns in M[][]

    S = [[0 for k in range(C)] for l in range(R)]
    # here we have set the first row and column of S[][]

    # Construct other entries
    for i in range(1, R):
        for j in range(1, C):
            if (M[i][j] == '.'):
                S[i][j] = min(S[i][j - 1], S[i - 1][j],
                              S[i - 1][j - 1]) + 1
            else:
                S[i][j] = 0

    # Find the maximum entry and
    # indices of maximum entry in S[][]
    max_of_s = S[0][0]
    max_i = 0
    max_j = 0
    for i in range(R):
        for j in range(C):
            if (max_of_s < S[i][j]):
                max_of_s = S[i][j]
                max_i = i
                max_j = j

    print("Maximum size sub-matrix is: ")
    for i in range(max_i, max_i - max_of_s, -1):
        for j in range(max_j, max_j - max_of_s, -1):
            print(M[i][j], end=" ")
            M[i][j]='x'
        #print("")
    return M

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print('Missing parameters.')
        exit()
    else:
        m=map_gen(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
        M=printMaxSubSquare(m)
    for i in range(int(sys.argv[2])):
        for j in range(int(sys.argv[1])):
            print(M[i][j],end='')
        print('')
