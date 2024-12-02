KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, koko):
        return [0] * koko
    
    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        if kapasiteetti is not None and (type(kapasiteetti) != int or kapasiteetti < 0):
            raise Exception("Väärä kapasiteetti")  # heitin vaan jotain :D

        self.kapasiteetti = kapasiteetti or KAPASITEETTI
        self.kasvatuskoko = kasvatuskoko or OLETUSKASVATUS

        self.alkioiden_lkm = 0
        self.taulukko = self._luo_lista(self.kapasiteetti)

    def kuuluu(self, n):
        return n in self.taulukko[:self.alkioiden_lkm]

    def lisaa(self, n):
        if self.kuuluu(n):
            return False

        self.taulukko[self.alkioiden_lkm] = n
        self.alkioiden_lkm = self.alkioiden_lkm + 1

        if self.alkioiden_lkm == 1:
            return True

        # ei mahdu enempää, luodaan uusi säilytyspaikka luvuille
        if self.alkioiden_lkm % len(self.taulukko) == 0:
            taulukko = self._luo_lista(self.alkioiden_lkm + self.kasvatuskoko)
            self.kopioi_lista(self.taulukko, taulukko)
            self.taulukko = taulukko

        return True

    def poista(self, n):
        if n not in self.taulukko:
            return False

        kohta = self.taulukko.index(n)
        self.taulukko = self.taulukko[:kohta] + self.taulukko[kohta + 1:] + [0]
        self.alkioiden_lkm = self.alkioiden_lkm - 1

        return True

    def kopioi_lista(self, a, b):
        for i in range(0, len(a)):
            b[i] = a[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        taulu = self._luo_lista(self.alkioiden_lkm)
        self.kopioi_lista(self.taulukko[:self.alkioiden_lkm], taulu)

        return taulu

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        [x.lisaa(n) for n in a.to_int_list()]
        [x.lisaa(n) for n in b.to_int_list()]

        return x

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        [y.lisaa(n) for n in a.to_int_list() if n in b.to_int_list()]

        return y

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()
        [z.lisaa(n) for n in a.to_int_list() if n not in b.to_int_list()]

        return z

    def __str__(self):
        return f"{{{ ", ".join([str(n) for n in self.taulukko[:self.alkioiden_lkm]]) }}}"
