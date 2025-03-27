from random import randint

class LosujKosci:
    def __init__(self, ile_rzutow):
        self.ile_rzutow = ile_rzutow
        self.rzuty = []
        self.zliczone = []
        self.wynik = 0

    def losowanie(self):
        for i in range(self.ile_rzutow):
            self.rzuty.append(randint(1, 6))
            print(f"Kość {i+1}: {self.rzuty[i]}")

    def sumowanie(self):
        for x in range(6):
            self.zliczone.append(self.rzuty.count(x+1))

    def zliczanie(self):
        c = 0
        for x in range(6):
            c += 1
            if self.zliczone[x] > 1:
                self.wynik += self.zliczone[x] * c
        print(f"Liczba uzyskanych punktów: {self.wynik}")

if __name__ == '__main__':
    while True:
        ile_razy = int(input("Ile kostek chcesz rzucić?(3 - 10): "))
        if 3 <= ile_razy <= 10:
            while True:
                lk = LosujKosci(ile_razy)
                lk.losowanie()
                lk.sumowanie()
                lk.zliczanie()

                powtorz = input("Jeszcze raz? (t/n)").capitalize()
                if powtorz == 'N':
                    break
            else:
                continue
        else:
            continue
        break
