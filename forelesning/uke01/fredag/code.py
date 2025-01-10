class Flaske:
    def __init__(self):
        self.kork = True

    def open(self):
        self.kork = False

    def drikk(self):
        if(self.kork):
            print("Kan ikke drikke, korka er på")
        else:
            print("Nam")

class DrikkeFlaske(Flaske):
    def __init__(self):
        self.kork = False

class Kopp:
    def __init__(self):
        pass

    def drikk(self):
        print("Det var god kaffe")


print("NY KJØRING")
flasker = []
for _ in range(4):
    flasker.append(Flaske())

flasker.append(DrikkeFlaske())

flasker[2].open()

flasker.append(Kopp())

for f in flasker:
    f.drikk()
