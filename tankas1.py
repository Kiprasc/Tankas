class Tankas:
    def __init__(self):
        self.x = []
        self.y = []
        self.kryptis = ["nesugeneruota"]
        self.suviu_skaicius_kryptis = {"Šuvis i šiaure: ": 0, "Šuvis i pietus: ": 0, "Šuvis i rytus: ": 0,
                                       "Šuvis i vakarus: ": 0}


    def pozicija(self):
        print("x: ", sum(self.x), "y: ", sum(self.y))

    def pirmyn(self):
        self.y.append(1)
        self.kryptis[0] = "šiaurė"

    def atgal(self):
        self.y.append(-1)
        self.kryptis[0] = "pietus"

    def kairen(self):
        self.x.append(-1)
        self.kryptis[0] = "vakarai"

    def desinen(self):
        self.x.append(1)
        self.kryptis[0] = "rytai"

    def tanko_kryptis(self):
        print("Tanko kryptis: ", self.kryptis[0])


    def info(self):
        print("Tanko kryptis: ", self.kryptis[0])
        print("Tankas išviso išovė kartų: ", sum(self.suviu_skaicius_kryptis.values()))
        print("Šuviu į šiaurę: ", self.suviu_skaicius_kryptis["Šuvis i šiaure: "], "\nŠuviu į rytus: ", self.suviu_skaicius_kryptis["Šuvis i rytus: "], "\nŠuviu į vakarus: ", self.suviu_skaicius_kryptis["Šuvis i vakarus: "], "\nŠuviu į pietus: ", self.suviu_skaicius_kryptis["Šuvis i pietus: "])

    def saudyti(self):
        if self.kryptis[0] == "šiaurė":
            self.suviu_skaicius_kryptis["Šuvis i šiaure: "] += 1
            print("Šuviu į šiaurę: ", self.suviu_skaicius_kryptis["Šuvis i šiaure: "])

        elif self.kryptis[0] == "pietus":
            self.suviu_skaicius_kryptis["Šuvis i pietus: "] += 1
            print("Šuviu į pietus: ", self.suviu_skaicius_kryptis["Šuvis i pietus: "])
            # print("Tankas išovė kartų: ", sum(self.suviu_skaicius_kryptis.values()))

        elif self.kryptis[0] == "vakarai":
            self.suviu_skaicius_kryptis["Šuvis i vakarus: "] += 1
            print("Šuviu į vakarus: ", self.suviu_skaicius_kryptis["Šuvis i vakarus: "])

        elif self.kryptis[0] == "rytai":
            self.suviu_skaicius_kryptis["Šuvis i rytus: "] += 1
            print("Šuviu į rytus: ", self.suviu_skaicius_kryptis["Šuvis i rytus: "])



        return


tankas = Tankas()

while True:
    print("Pasirinkite veiksmą: ")
    print("w - Judėti pirmyn")
    print("s - Judėti žemyn")
    print("a - Judėti i kaire")
    print("d - Judėti i dešine")
    print("x - Šaudyti")
    print("i - INFO")
    print("0 - Baigti zaidima")

    pasirinkimas = input()

    if pasirinkimas == "w":
        tankas.pirmyn()
        print("Pozicija: ")
        tankas.pozicija()
        tankas.tanko_kryptis()


    if pasirinkimas == "s":
        tankas.atgal()
        print("Pozicija: ")
        tankas.pozicija()
        tankas.tanko_kryptis()


    if pasirinkimas == "a":
        tankas.kairen()
        print("Pozicija: ")
        tankas.pozicija()
        tankas.tanko_kryptis()


    if pasirinkimas == "d":
        tankas.desinen()
        print("Pozicija: ")
        tankas.pozicija()
        tankas.tanko_kryptis()


    if pasirinkimas == "x":
        tankas.saudyti()
        tankas.pozicija()
        tankas.tanko_kryptis()

    if pasirinkimas == "i":
        tankas.info()

    if pasirinkimas == "0":
        print("Žaidimo pabaiga")
        break
