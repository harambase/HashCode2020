import numpy as np
import time


# N: number of different pizza, K: max slices
def Pizza():
    p = np.zeros(shape=(N, K))
    s = np.zeros(shape=(N, K))
    for n in range(0, N):
        for k in range(0, K):
            if n == k and n == 0:
                p[n][k] = 1
                s[n][k] = 0
            elif n == 0 and k > 0:
                p[0][k] = 0
                s[0][k] = 0
            elif n > 0 and k == 0:
                p[n][0] = 1
                s[n][0] = 0
            else:
                if x[n] > k:
                    p[n][k] = p[n - 1][k]
                    s[n][k] = 0
                elif x[n] == k:
                    p[n][k] = 1
                    s[n][k] = 1
                elif x[n] < k:
                    p[n][k] = max(p[n - 1][k], p[n - 1][k - x[n]])
                    if p[n][k] == 0:
                        s[n][k] = 0
                    elif p[n - 1][k - x[n]] == 1:
                        s[n][k] = 1
                    else:
                        s[n][k] = 0

    k = K
    n = 0
    result = []
    visited = False
    while k > 0:
        if not visited:
            k -= 1
        while n < N:
            if s[n][k] == 1:
                result.append(x[n])
                k = k - x[n]
                n = 0
                visited = True
            n += 1
    print(np.sum(result))
    print(result)


def main():
    global N, K, x
    f = open("d_quite_big.in", "r")
    contents = f.readlines()

    K = int(contents[0].split(" ")[0])
    N = int(contents[0].split(" ")[1]) + 1
    x = np.array(contents[1].split(" "), int)
    x = np.append(0, x)
    f.close()

    start_time = time.time()
    Pizza()
    end_time = time.time()
    print("The time was %g seconds" % (end_time - start_time))


if __name__ == "__main__":
    # execute only if run as a script
    main()
