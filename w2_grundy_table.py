#! python3


def mex(nums) -> int:
    '''
    Find the smallest non-negative integer in a list by create a Python set
    '''
    tmp = set(nums)
    cnt = 0
    for t in tmp:
        if t != cnt:
            return cnt
        cnt += 1
    return cnt


def findGrundy(G: list, V: int, W: int) -> list:
    for v in range(1, V + 1):
        for w in range(1, W+1):
            if v == w:
                continue
            if not G[v][w]:
                positions = []
                for i in range(v):
                    positions.append(G[i][w])
                for j in range(w):
                    positions.append(G[v][j])
                G[v][w] = mex(positions)

if __name__ == "__main__":
    V = 4  # Size of the first pile
    W = 4  # Size of the second pile
    G = [[None for _ in range(W+1)] for _ in range(V+1)] # Grundy Table G(V,W)

    # Initialize boundary cases:
    # G(i,0) and G(0,i) are winning positions
    for i in range(V+1):
        G[i][0] = i
    for j in range(W+1):
        G[0][j] = j
    # G(i,i) are losing postions
    for i in range(min(V+1, W+1)):
        G[i][i] = 0

    findGrundy(G, V, W)
    print("GrundyTable of dimension (V,W):")
    for i in range(V+1):
        print(G[i])

    # Check mex:
    # nums = [1, 1, 6, 2]
    # print(mex(nums))
