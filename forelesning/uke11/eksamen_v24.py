
class Kjølebil:

    def __init__(self, område):
        self.område = område

    def legg_til_vare(self, navn, ant):
        print("Bruk de andre klassene")

    def __str__(self):
        return "Kjølebil i området " + self.område
    
class Isbil(Kjølebil):

    def __init__(self, område, sortiment):
        super().__init__(område)
        self.sortiment = sortiment
        self.vareantall = {}
        for vare in sortiment:
            self.vareantall[vare] = 0
    
    def legg_til_vare(self, navn, ant):
        if not navn in self.sortiment:
            raise ValueError("Vare ikke funnet")
        self.vareantall[navn] += ant

    def selg(self, navn, ant):
        if not navn in self.sortiment:
            raise ValueError("Vare ikke funnet")
        if self.vareantall[navn] - ant < 0:
            print("Bilen er tom, du får bare", \
                  self.vareantall[navn])
            self.vareantall[navn] = 0
        else:
            self.vareantall[navn] -= ant

class Fiskebil(Kjølebil):

    def __init__(self, område):
        super().__init__(område)
        self.varer = []
        self.ant_varer = 0

    def legg_til_vare(self, navn, ant):
        if ant + self.ant_varer > 10:
            raise ValueError("For mange varer")
        self.varer.append(navn)
        self.ant_varer += ant

    def kjør_ut(self):
        self.varer = []
        self.ant_varer = 0


class Administrasjonssystem:

    def __init__(self):
        self.biler = []
        self.issortiment = []

    def legg_til_ny_is(self, varenavn):
        self.issortiment.append(varenavn)

    def legg_til_bil(self, biltype, område):
        if biltype == "fiskebil":
            self.biler.append(Fiskebil(område))
        elif biltype == "isbil":
            self.biler.append(Isbil(område,
                                    self.issortiment))
        else:
            print("Ukjent type bil")

    def fiskebestilling(self, område, fisketype, antall):
        for bil in self.biler:
            if isinstance(bil, Fiskebil):
                if bil.område == område:
                    if bil.ant_varer + antall <= 10:
                        bil.legg_til_vare(fisketype, antall)
                        return
        print("Kunne ikke legge til bestilling")

    def kjør_ut_fisk(self):
        for bil in self.biler:
            if isinstance(bil, Fiskebil):
                bil.kjør_ut()

    def __str__(self):
        ant_fisk = 0
        ant_is = 0
        for bil in self.biler:
            if isinstance(bil, Fiskebil):
                ant_fisk += 1
            else:
                ant_is += 1
        return f"Vi eier {ant_is} isbiler og {ant_fisk} \
                fiskebiler"