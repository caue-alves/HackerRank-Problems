def average(array):
    # your code goes here
    nSet = set(array)
    return sum(list(nSet)) / len(list(nSet))
    

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)