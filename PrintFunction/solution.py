if __name__ == '__main__':
    n = int(input())
    final = 1
    f = []
    while final <= n:
        f.append(str(final))
        final += 1
    print("".join(f))