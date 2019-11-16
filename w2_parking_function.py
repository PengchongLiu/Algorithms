
def nParking(n):
    # http://www-math.mit.edu/~rstan/transparencies/parking.pdf
    return (n+1)**(n-1)


def parking(n):
    res = []
    res.append([(1,)])
    for i in range(1, n):
        prev_set = res.pop()
        new_set = []
        for prev in prev_set:
            for pos in range(i+1):
                for j in range(i + 1):
                    tmp = prev[:pos]+(j+1,)+(prev[pos:])
                    if tmp not in new_set:
                        new_set.append(tmp)
        res.append(new_set)
    return res[0]


if __name__ == "__main__":
    n = int(input("Number of spots: "))
    res = parking(n)
    print("Find all possible functions?", len(res) == nParking(n))
    print("Functions found: %d\n" % len(res), res)
