import numpy as np
import time


# N: number of different pizza, K: max slices
def Pizza():

    p = np.zeros(shape=(N, int(1e7)), dtype=int)
    s = np.zeros(shape=(N, int(1e7)), dtype=int)

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
    return result


def main():
    global N, K, x
    name = "a_example"
    # name = "b_small"
    name = "c_medium"
    #name = "d_quite_big"

    fin = open(name + ".in", "r")
    contents = fin.readlines()

    K = np.long(contents[0].split(" ")[0])
    N = np.long(contents[0].split(" ")[1]) + 1

    x = np.array(contents[1].split(" "), int)
    x = np.append(0, x)
    fin.close()

    start_time = time.time()
    result = Pizza()
    end_time = time.time()

    fout = open(name + ".out", "w+")
    fout.write('%g\n' % len(result))
    for i in range(0, len(result)):
        fout.write('%g ' % result[len(result) - i - 1])
    print("The time was %g seconds" % (end_time - start_time))


if __name__ == "__main__":
    # execute only if run as a script
    main()
