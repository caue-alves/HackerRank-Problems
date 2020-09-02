if __name__ == '__main__':
    n = int(input())
    i = 0
    l = []
    while i <= n:
        l.append(i)
        i+=1
    for it in l[:len(l) - 1]:
        print(it**2)