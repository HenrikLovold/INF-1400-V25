
def fak_iter(n):
    fak = 1
    for i in range(1, n+1):
        fak = fak*i
    return fak

def fak_rec(n):
    if n == 1:
        return 1
    return fak_rec(n-1) * n

if __name__ == "__main__":
    print(fak_iter(5))
    print(fak_rec(5))