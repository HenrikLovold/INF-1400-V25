class Eksponent:
    def __init__(self, verdi):
        self.val = verdi

    def eksponensier(self, potens):
        return self.val ** potens

def eksponent(verdi, potens):
    return verdi ** potens

if __name__ == "__main__":
    print("NY KJØRING")
    e = Eksponent(4)
    print(e.eksponensier(3))
    print(eksponent(4, 3))
