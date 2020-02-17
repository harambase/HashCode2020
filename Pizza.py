import numpy as np
import time


# N: number of different pizza, K: max slices
def Pizza():
    offset = i = 0
    result = []

    if K > 1e6:
        while K - offset > 2e5:
            index = len(x) - i - 1
            offset += x[index]
            result.append(x[index])
            i += 1
    print(i)
    p = np.zeros(shape=(N - i, K - offset), dtype=int)
    s = np.zeros(shape=(N - i, K - offset), dtype=int)

    x0 = x[0]
    for n in range(x0, N - i):
        for k in range(x0, K - offset):
            if n == k and n == x0:
                p[n][k] = 1
                s[n][k] = 0
            elif n == x0 and k > x0:
                p[x0][k] = 0
                s[x0][k] = 0
            elif n > x0 and k == x0:
                p[n][x0] = 1
                s[n][x0] = 0
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

    k = K - offset
    n = 0
    visited = False
    while k > 0:
        if not visited:
            k -= 1
        while n < N - i:
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
    #name = "a_example"
    #name = "b_small"
    #name = "c_medium"
    name = "d_quite_big"
    #name = "e_also_big"

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
