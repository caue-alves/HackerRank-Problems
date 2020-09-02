import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    alice = []
    bob = []
    for i in list(range(len(a))):
        if a[i] > b[i]:
            alice.append(True)
        else:
            alice.append(False)
        if b[i] > a[i]:
            bob.append(True)
        else:
            bob.append(False)
    return [sum(alice), sum(bob)]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()