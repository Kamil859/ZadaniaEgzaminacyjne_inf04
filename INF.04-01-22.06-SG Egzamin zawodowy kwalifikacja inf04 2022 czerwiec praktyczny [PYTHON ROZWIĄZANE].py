from random import randint

class SzukanieWartownika:
    def __init__(self, szukany):
        self.szukany = szukany
        self.zbior = []

    def losowanie_elementow(self):
        for x in range(50):
            losowa = randint(1, 100)
            self.zbior.append(losowa)
        self.zbior.append(self.szukany)
        print(f"Elementy wylosowane: {self.zbior}")

    def szukanie_elementu(self):
        for x in range(len(self.zbior)-1):
            if self.szukany not in self.zbior[0:-2]:
                print("Nie znaleziono wartownika!")
                break
            else:
                print(f"Znaleziono wartownika [index: {self.zbior.index(self.szukany)}]")
                break

if __name__ == '__main__':
    szukam = int(input("Podaj wartość do szukania: "))
    sw = SzukanieWartownika(szukam)
    sw.losowanie_elementow()
    sw.szukanie_elementu()