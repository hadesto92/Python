import numpy as np
import matplotlib.pyplot as plt
import math


class Punkt():
    def __init__(self,n):
        self.x = round(np.random.rand()*n,0)
        self.y = round(np.random.rand()*n,0)


class Trojkat():
    def __init__(self,n):
        self.skala_osi = n
        self.A = Punkt(self.skala_osi)
        self.B = Punkt(self.skala_osi)
        self.C = Punkt(self.skala_osi)

        self.AB = round(math.sqrt((self.B.x - self.A.x) ** 2 + (self.B.y - self.A.y) ** 2), 2)
        self.BC = round(math.sqrt((self.C.x - self.B.x) ** 2 + (self.C.y - self.B.y) ** 2), 2)
        self.CA = round(math.sqrt((self.A.x - self.C.x) ** 2 + (self.A.y - self.C.y) ** 2), 2)

        self.p = round(self.obwod() / 2, 2)

        while self.p == self.AB or self.p == self.BC or self.p == self.CA:
            self.A = Punkt(self.skala_osi)
            self.B = Punkt(self.skala_osi)
            self.C = Punkt(self.skala_osi)

            self.AB = round(math.sqrt((self.B.x - self.A.x) ** 2 + (self.B.y - self.A.y) ** 2),2)
            self.BC = round(math.sqrt((self.C.x - self.B.x) ** 2 + (self.C.y - self.B.y) ** 2),2)
            self.CA = round(math.sqrt((self.A.x - self.C.x) ** 2 + (self.A.y - self.C.y) ** 2),2)

            self.p = round(self.obwod() / 2,2)


    def draw(self):
        x = [self.A.x, self.B.x, self.C.x, self.A.x]
        y = [self.A.y, self.B.y, self.C.y, self.A.y]
        plt.plot(x, y)
        plt.grid()

    def drawShow(self):
        plt.show()

    def pole(self):
        pole = math.sqrt((self.p*((self.p-self.AB)*(self.p-self.BC)*(self.p-self.CA))))
        return round(pole,2)

    def obwod(self):
        return self.AB+self.BC+self.CA

class Prostokat():
    def __init__(self,n):
        self.skala_osi = n
        self.A = Punkt(self.skala_osi)
        self.B = Punkt(self.skala_osi)
        self.C = Punkt(self.skala_osi)
        self.D = Punkt(self.skala_osi)

        self.wyszukanie()

        self.AB = round(math.sqrt((self.B.x - self.A.x) ** 2 + (self.B.y - self.A.y) ** 2), 0)
        self.BC = round(math.sqrt((self.C.x - self.B.x) ** 2 + (self.C.y - self.B.y) ** 2), 0)
        self.CD = round(math.sqrt((self.D.x - self.C.x) ** 2 + (self.D.y - self.C.y) ** 2), 0)
        self.DA = round(math.sqrt((self.A.x - self.D.x) ** 2 + (self.A.y - self.D.y) ** 2), 0)

        self.p = round(self.obwod()/2,0)

    def draw(self, index):

        x = [self.A.x, self.B.x, self.C.x, self.D.x, self.A.x]
        y = [self.A.y, self.B.y, self.C.y, self.D.y, self.A.y]

        x1 = [self.A.x]
        y1 = [self.A.y]

        x2 = [self.B.x]
        y2 = [self.B.y]

        x3 = [self.C.x]
        y3 = [self.C.y]

        x4 = [self.D.x]
        y4 = [self.D.y]

        plt.subplot(5,5,index+1)
        plt.plot(x, y)
        plt.plot(x1, y1, 'o')
        plt.plot(x2, y2, '*')
        plt.plot(x3, y3, 's')
        plt.plot(x4, y4, 'd')

        plt.grid()

    def wyszukanie(self):
        flaga = 0
        while flaga == 0:
            if self.A.x > int(self.skala_osi/2) or self.A.y > int(self.skala_osi/2):
                self.A = Punkt(self.skala_osi)
            else:
                flaga=1
        flaga = 0
        while flaga == 0:
            if self.B.x > int(self.skala_osi/2) or self.B.y <= self.A.y:
                self.B = Punkt(self.skala_osi)
            else:
                flaga = 1
        flaga = 0
        while flaga == 0:
            if self.C.x <= self.B.x or self.C.y <= int(self.skala_osi/2):
                self.C = Punkt(self.skala_osi)
            else:
                flaga = 1
        flaga = 0
        while flaga == 0:
            if self.D.x <= self.A.x or self.D.x <= self.B.x or self.D.y >= self.B.y or self.D.y >= self.C.y:
                self.D = Punkt(self.skala_osi)
            else:
                flaga = 1

    def drawShow(self):
        plt.show()

    def pole(self):
        return round(math.sqrt((self.p-self.AB)*(self.p-self.BC)*(self.p-self.CD)*(self.p-self.DA)),2)

    def obwod(self):
        return self.AB + self.BC + self.CD + self.DA
    """    
    def wyszukanie(self,tab): #przejżeć czy to daje radę dla punktów (10,0) (10,10) (0,10)

        najkrotsza = min(tab)

        index = []

        for i in range(len(tab)):
            if najkrotsza == tab[i]:
                index.append(i)

        if len(index) == 1:
            self.temp_tab.append(self.copy_tab_p[index[0]])
            del self.copy_tab_p[index[0]]
        elif len(index) == 2:
            if self.copy_tab_p[index[0]].x < self.copy_tab_p[index[1]].x:
                self.temp_tab.append(self.copy_tab_p[index[0]])
                del self.copy_tab_p[index[0]]
            else:
                self.temp_tab.append(self.copy_tab_p[index[1]])
                del self.copy_tab_p[index[1]]
        elif len(index) == 3:
            if self.copy_tab_p[index[1]].x < self.copy_tab_p[index[0]].x < self.copy_tab_p[index[2]].x:
                self.temp_tab.append(self.copy_tab_p[index[0]])
                del self.copy_tab_p[index[0]]
            elif self.copy_tab_p[index[2]].x < self.copy_tab_p[index[0]].x < self.copy_tab_p[index[1]].x:
                self.temp_tab.append(self.copy_tab_p[index[0]])
                del self.copy_tab_p[index[0]]
            elif self.copy_tab_p[index[0]].x < self.copy_tab_p[index[1]].x < self.copy_tab_p[index[2]].x:
                self.temp_tab.append(self.copy_tab_p[index[1]])
                del self.copy_tab_p[index[1]]
            elif self.copy_tab_p[index[2]].x < self.copy_tab_p[index[1]].x < self.copy_tab_p[index[0]].x:
                self.temp_tab.append(self.copy_tab_p[index[1]])
                del self.copy_tab_p[index[1]]
            else:
                self.temp_tab.append(self.copy_tab_p[index[2]])
                del self.copy_tab_p[index[2]]
        else:
            if self.copy_tab_p[index[0]].x < self.copy_tab_p[index[1]].x:
                if self.copy_tab_p[index[0]].x < self.copy_tab_p[index[2]].x:
                    if self.copy_tab_p[index[0]].x < self.copy_tab_p[index[3]].x:
                        self.temp_tab.append(self.copy_tab_p[index[0]])
                        del self.copy_tab_p[index[0]]
                    else:
                        self.temp_tab.append(self.copy_tab_p[index[3]])
                        del self.copy_tab_p[index[3]]
                else:
                    if self.copy_tab_p[index[2]].x < self.copy_tab_p[index[3]].x:
                        self.temp_tab.append(self.copy_tab_p[index[2]])
                        del self.copy_tab_p[index[2]]
                    else:
                        self.temp_tab.append(self.copy_tab_p[index[3]])
                        del self.copy_tab_p[index[3]]
            else:
                if self.copy_tab_p[index[1]].x < self.copy_tab_p[index[2]].x:
                    if self.copy_tab_p[index[1]].x < self.copy_tab_p[index[3]].x:
                        self.temp_tab.append(self.copy_tab_p[index[1]])
                        del self.copy_tab_p[index[1]]
                    else:
                        self.temp_tab.append(self.copy_tab_p[index[3]])
                        del self.copy_tab_p[index[3]]
                else:
                    if self.copy_tab_p[index[2]].x < self.copy_tab_p[index[3]].x:
                        self.temp_tab.append(self.copy_tab_p[index[2]])
                        del self.copy_tab_p[index[2]]
                    else:
                        self.temp_tab.append(self.copy_tab_p[index[3]])
                        del self.copy_tab_p[index[3]]
    
    def zamiana_3(self):
        self.A = Punkt()
        self.B = Punkt()
        self.C = Punkt()
        self.D = Punkt()

    def wyszukanie_2(self,index):
        if index == 0:
            flaga = 0
            while flaga == 0:
                if self.A.x < self.B.x < self.C.x < self.D.x and self.A.y < self.B.y < self.C.y < self.D.y:
                    print(index)
                    flaga = 1
                else:
                    self.zamiana_3()
        elif index == 1:
            flaga = 0
            while flaga == 0:
                if self.A.x < self.B.x < self.D.x < self.C.x and self.A.y < self.B.y < self.C.y < self.D.y:
                    print(index)
                    flaga = 1
                else:
                    self.zamiana_3()
        elif index == 2:
            flaga = 0
            while flaga == 0:
                if self.A.x < self.C.x < self.B.x < self.D.x and self.A.y < self.B.y < self.C.y < self.D.y:
                    print(index)
                    flaga = 1
                else:
                    self.zamiana_3()
        elif index == 3:
            flaga = 0
            while flaga == 0:
                if self.A.x < self.C.x < self.D.x < self.B.x and self.A.y < self.B.y < self.C.y < self.D.y:
                    print(index)
                    flaga = 1
                else:
                    self.zamiana_3()
        elif index == 4:
            flaga = 0
            while flaga == 0:
                if self.A.x < self.D.x < self.B.x < self.C.x and self.A.y < self.B.y < self.C.y < self.D.y:
                    print(index)
                    flaga = 1
                else:
                    self.zamiana_3()
        elif index == 5:
            flaga = 0
            while flaga == 0:
                if self.A.x < self.D.x < self.C.x < self.B.x and self.A.y < self.B.y < self.C.y < self.D.y:
                    print(index)
                    flaga = 1
                else:
                    self.zamiana_3()
        elif index == 6:
            flaga = 0
            while flaga == 0:
                if self.B.x < self.A.x < self.C.x < self.D.x and self.A.y < self.B.y < self.C.y < self.D.y:
                    print(index)
                    flaga = 1
                else:
                    self.zamiana_3()
        elif index == 7:
            flaga = 0
            while flaga == 0:
                if self.B.x < self.A.x < self.D.x < self.C.x and self.A.y < self.B.y < self.C.y < self.D.y:
                    print(index)
                    flaga = 1
                else:
                    self.zamiana_3()
        elif index == 8:
            flaga = 0
            while flaga == 0:
                if self.B.x < self.C.x < self.A.x < self.D.x and self.A.y < self.B.y < self.C.y < self.D.y:
                    print(index)
                    flaga = 1
                else:
                    self.zamiana_3()
        elif index == 9:
            flaga = 0
            while flaga == 0:
                if self.B.x < self.C.x < self.D.x < self.A.x and self.A.y < self.B.y < self.C.y < self.D.y:
                    print(index)
                    flaga = 1
                else:
                    self.zamiana_3()
        elif index == 10:
            flaga = 0
            while flaga == 0:
                if self.B.x < self.D.x < self.A.x < self.C.x and self.A.y < self.B.y < self.C.y < self.D.y:
                    print(index)
                    flaga = 1
                else:
                    self.zamiana_3()
        elif index == 11:
            flaga = 0
            while flaga == 0:
                if self.B.x < self.D.x < self.C.x < self.A.x and self.A.y < self.B.y < self.C.y < self.D.y:
                    print(index)
                    flaga = 1
                else:
                    self.zamiana_3()
        elif index == 12:
            flaga = 0
            while flaga == 0:
                if self.C.x < self.A.x < self.B.x < self.D.x and self.A.y < self.B.y < self.C.y < self.D.y:
                    print(index)
                    flaga = 1
                else:
                    self.zamiana_3()
        elif index == 13:
            flaga = 0
            while flaga == 0:
                if self.C.x < self.A.x < self.D.x < self.B.x and self.A.y < self.B.y < self.C.y < self.D.y:
                    print(index)
                    flaga = 1
                else:
                    self.zamiana_3()
        elif index == 14:
            flaga = 0
            while flaga == 0:
                if self.C.x < self.B.x < self.A.x < self.D.x and self.A.y < self.B.y < self.C.y < self.D.y:
                    print(index)
                    flaga = 1
                else:
                    self.zamiana_3()
        elif index == 15:
            flaga = 0
            while flaga == 0:
                if self.C.x < self.B.x < self.D.x < self.A.x and self.A.y < self.B.y < self.C.y < self.D.y:
                    print(index)
                    flaga = 1
                else:
                    self.zamiana_3()
        elif index == 16:
            flaga = 0
            while flaga == 0:
                if self.C.x < self.D.x < self.A.x < self.B.x and self.A.y < self.B.y < self.C.y < self.D.y:
                    print(index)
                    flaga = 1
                else:
                    self.zamiana_3()
        elif index == 17:
            flaga = 0
            while flaga == 0:
                if self.C.x < self.D.x < self.B.x < self.A.x and self.A.y < self.B.y < self.C.y < self.D.y:
                    print(index)
                    flaga = 1
                else:
                    self.zamiana_3()
        elif index == 18:
            flaga = 0
            while flaga == 0:
                if self.D.x < self.A.x < self.B.x < self.C.x and self.A.y < self.B.y < self.C.y < self.D.y:
                    print(index)
                    flaga = 1
                else:
                    self.zamiana_3()
        elif index == 19:
            flaga = 0
            while flaga == 0:
                if self.D.x < self.A.x < self.C.x < self.B.x and self.A.y < self.B.y < self.C.y < self.D.y:
                    print(index)
                    flaga = 1
                else:
                    self.zamiana_3()
        elif index == 20:
            flaga = 0
            while flaga == 0:
                if self.D.x < self.B.x < self.A.x < self.C.x and self.A.y < self.B.y < self.C.y < self.D.y:
                    print(index)
                    flaga = 1
                else:
                    self.zamiana_3()
        elif index == 21:
            flaga = 0
            while flaga == 0:
                if self.D.x < self.B.x < self.C.x < self.A.x and self.A.y < self.B.y < self.C.y < self.D.y:
                    print(index)
                    flaga = 1
                else:
                    self.zamiana_3()
        elif index == 22:
            flaga = 0
            while flaga == 0:
                if self.D.x < self.C.x < self.A.x < self.B.x and self.A.y < self.B.y < self.C.y < self.D.y:
                    print(index)
                    flaga = 1
                else:
                    self.zamiana_3()
        elif index == 23:
            flaga = 0
            while flaga == 0:
                if self.D.x < self.C.x < self.B.x < self.A.x and self.A.y < self.B.y < self.C.y < self.D.y:
                    print(index)
                    flaga = 1
                else:
                    self.zamiana_3()
    
    def zamiana_2(self):
        index_1 = np.random.randint(1, 4)
        index_2 = np.random.randint(1, 4)

        while index_1 == index_2:
            index_1 = np.random.randint(1, 4)
            index_2 = np.random.randint(1, 4)

        self.temp_tab[index_1], self.temp_tab[index_2] = self.temp_tab[index_2], self.temp_tab[index_1]

    def if_wykluczenie(self,a,b,c,d,e,f,g,h):
        if self.temp_tab[a].x < self.temp_tab[b].x < self.temp_tab[c].x < self.temp_tab[d].x and self.temp_tab[e].y < self.temp_tab[f].y < self.temp_tab[g].y < self.temp_tab[h].y:
            self.zamiana_2()
            return True
        else:
            return False

    def wykluczenie(self):
        flaga = 0
        while flaga == 0:
            if self.temp_tab[0].x < self.temp_tab[1].x < self.temp_tab[2].x < self.temp_tab[3].x and self.temp_tab[0].y < self.temp_tab[3].y < self.temp_tab[2].y < self.temp_tab[1].y:
                self.zamiana_2()
                continue
            elif self.temp_tab[0].x < self.temp_tab[1].x < self.temp_tab[3].x < self.temp_tab[2].x and self.temp_tab[0].y < self.temp_tab[1].y < self.temp_tab[2].y < self.temp_tab[3].y:
                self.zamiana_2()
                continue
            elif self.temp_tab[0].x < self.temp_tab[1].x < self.temp_tab[3].x < self.temp_tab[2].x and self.temp_tab[0].y < self.temp_tab[1].y < self.temp_tab[3].y < self.temp_tab[2].y:
                self.zamiana_2()
                continue
            elif self.temp_tab[0].x < self.temp_tab[1].x < self.temp_tab[3].x < self.temp_tab[2].x and self.temp_tab[0].y < self.temp_tab[3].y < self.temp_tab[1].y < self.temp_tab[2].y:
                self.zamiana_2()
                continue
            elif self.temp_tab[0].x < self.temp_tab[1].x < self.temp_tab[3].x < self.temp_tab[2].x and self.temp_tab[0].y < self.temp_tab[3].y < self.temp_tab[2].y < self.temp_tab[1].y:
                self.zamiana_2()
                continue
            elif self.temp_tab[0].x < self.temp_tab[3].x < self.temp_tab[1].x < self.temp_tab[2].x and self.temp_tab[0].y < self.temp_tab[2].y < self.temp_tab[3].y < self.temp_tab[1].y:
                self.zamiana_2()
                continue
            elif self.temp_tab[1].x < self.temp_tab[0].x < self.temp_tab[2].x < self.temp_tab[3].x and self.temp_tab[0].y < self.temp_tab[3].y < self.temp_tab[1].y < self.temp_tab[2].y:
                self.zamiana_2()
                continue
            elif self.temp_tab[1].x < self.temp_tab[0].x < self.temp_tab[3].x < self.temp_tab[2].x and self.temp_tab[0].y < self.temp_tab[1].y < self.temp_tab[2].y < self.temp_tab[3].y:
                self.zamiana_2()
                continue
            elif self.temp_tab[1].x < self.temp_tab[0].x < self.temp_tab[3].x < self.temp_tab[2].x and self.temp_tab[0].y < self.temp_tab[3].y < self.temp_tab[2].y < self.temp_tab[1].y:
                self.zamiana_2()
                continue
            elif self.temp_tab[1].x < self.temp_tab[3].x < self.temp_tab[2].x < self.temp_tab[0].x and self.temp_tab[0].y < self.temp_tab[2].y < self.temp_tab[3].y < self.temp_tab[1].y:
                self.zamiana_2()
                continue
            elif self.temp_tab[1].x < self.temp_tab[3].x < self.temp_tab[0].x < self.temp_tab[2].x and self.temp_tab[2].y < self.temp_tab[0].y < self.temp_tab[3].y < self.temp_tab[1].y:
                self.zamiana_2()
                continue
            elif self.temp_tab[0].x < self.temp_tab[1].x < self.temp_tab[2].x < self.temp_tab[3].x and self.temp_tab[3].y < self.temp_tab[0].y < self.temp_tab[1].y < self.temp_tab[2].y:
                self.zamiana_2()
                continue
            elif self.temp_tab[0].x < self.temp_tab[1].x < self.temp_tab[2].x < self.temp_tab[3].x and self.temp_tab[3].y < self.temp_tab[0].y < self.temp_tab[2].y < self.temp_tab[1].y:
                self.zamiana_2()
                continue
            elif self.temp_tab[0].x < self.temp_tab[1].x < self.temp_tab[2].x < self.temp_tab[3].x and self.temp_tab[3].y < self.temp_tab[2].y < self.temp_tab[0].y < self.temp_tab[1].y:
                self.zamiana_2()
                continue
            elif self.temp_tab[0].x < self.temp_tab[1].x < self.temp_tab[3].x < self.temp_tab[2].x and self.temp_tab[3].y < self.temp_tab[0].y < self.temp_tab[1].y < self.temp_tab[2].y:
                self.zamiana_2()
                continue
            elif self.temp_tab[0].x < self.temp_tab[1].x < self.temp_tab[3].x < self.temp_tab[2].x and self.temp_tab[3].y < self.temp_tab[0].y < self.temp_tab[2].y < self.temp_tab[1].y:
                self.zamiana_2()
                continue
            elif self.temp_tab[0].x < self.temp_tab[1].x < self.temp_tab[3].x < self.temp_tab[2].x and self.temp_tab[3].y < self.temp_tab[2].y < self.temp_tab[0].y < self.temp_tab[1].y:
                self.zamiana_2()
                continue
            elif self.temp_tab[0].x < self.temp_tab[2].x < self.temp_tab[1].x < self.temp_tab[3].x and self.temp_tab[3].y < self.temp_tab[0].y < self.temp_tab[2].y < self.temp_tab[1].y:
                self.zamiana_2()
                continue
            elif self.temp_tab[0].x < self.temp_tab[3].x < self.temp_tab[1].x < self.temp_tab[2].x and self.temp_tab[3].y < self.temp_tab[0].y < self.temp_tab[2].y < self.temp_tab[1].y:
                self.zamiana_2()
                continue
            elif self.temp_tab[0].x < self.temp_tab[3].x < self.temp_tab[1].x < self.temp_tab[2].x and self.temp_tab[3].y < self.temp_tab[2].y < self.temp_tab[0].y < self.temp_tab[1].y:
                self.zamiana_2()
                continue
            elif self.temp_tab[1].x < self.temp_tab[0].x < self.temp_tab[2].x < self.temp_tab[3].x and self.temp_tab[3].y < self.temp_tab[0].y < self.temp_tab[1].y < self.temp_tab[2].y:
                self.zamiana_2()
                continue
            elif self.temp_tab[1].x < self.temp_tab[0].x < self.temp_tab[2].x < self.temp_tab[3].x and self.temp_tab[3].y < self.temp_tab[0].y < self.temp_tab[2].y < self.temp_tab[1].y:
                self.zamiana_2()
                continue
            elif self.temp_tab[1].x < self.temp_tab[0].x < self.temp_tab[3].x < self.temp_tab[2].x and self.temp_tab[3].y < self.temp_tab[0].y < self.temp_tab[1].y < self.temp_tab[2].y:
                self.zamiana_2()
                continue
            elif self.temp_tab[1].x < self.temp_tab[2].x < self.temp_tab[0].x < self.temp_tab[3].x and self.temp_tab[3].y < self.temp_tab[0].y < self.temp_tab[1].y < self.temp_tab[1].y:
                self.zamiana_2()
                continue
            elif self.temp_tab[1].x < self.temp_tab[2].x < self.temp_tab[0].x < self.temp_tab[3].x and self.temp_tab[3].y < self.temp_tab[0].y < self.temp_tab[2].y < self.temp_tab[1].y:
                self.zamiana_2()
                continue
            elif self.temp_tab[0].x < self.temp_tab[1].x < self.temp_tab[2].x < self.temp_tab[3].x and self.temp_tab[0].y < self.temp_tab[2].y < self.temp_tab[3].y < self.temp_tab[1].y:
                self.zamiana_2()
                continue
            elif self.temp_tab[0].x < self.temp_tab[1].x < self.temp_tab[2].x < self.temp_tab[3].x and self.temp_tab[0].y < self.temp_tab[3].y < self.temp_tab[1].y < self.temp_tab[2].y:
                self.zamiana_2()
                continue
            elif self.temp_tab[0].x < self.temp_tab[1].x < self.temp_tab[3].x < self.temp_tab[2].x and self.temp_tab[0].y < self.temp_tab[2].y < self.temp_tab[3].y < self.temp_tab[1].y:
                self.zamiana_2()
                continue
            elif self.temp_tab[0].x < self.temp_tab[2].x < self.temp_tab[3].x < self.temp_tab[1].x and self.temp_tab[0].y < self.temp_tab[3].y < self.temp_tab[2].y < self.temp_tab[1].y:
                self.zamiana_2()
                continue
            elif self.temp_tab[0].x < self.temp_tab[3].x < self.temp_tab[1].x < self.temp_tab[2].x and self.temp_tab[0].y < self.temp_tab[3].y < self.temp_tab[2].y < self.temp_tab[1].y:
                self.zamiana_2()
                continue
            elif self.temp_tab[1].x < self.temp_tab[0].x < self.temp_tab[2].x < self.temp_tab[3].x and self.temp_tab[0].y < self.temp_tab[3].y < self.temp_tab[2].y < self.temp_tab[1].y:
                self.zamiana_2()
                continue
            elif self.temp_tab[1].x < self.temp_tab[0].x < self.temp_tab[3].x < self.temp_tab[2].x and self.temp_tab[0].y < self.temp_tab[2].y < self.temp_tab[1].y < self.temp_tab[3].y:
                self.zamiana_2()
                continue
            elif self.temp_tab[1].x < self.temp_tab[0].x < self.temp_tab[3].x < self.temp_tab[2].x and self.temp_tab[0].y < self.temp_tab[3].y < self.temp_tab[1].y < self.temp_tab[2].y:
                self.zamiana_2()
                continue
            elif self.temp_tab[1].x < self.temp_tab[2].x < self.temp_tab[3].x < self.temp_tab[0].x and self.temp_tab[0].y < self.temp_tab[3].y < self.temp_tab[2].y < self.temp_tab[1].y:
                self.zamiana_2()
                continue
            elif self.temp_tab[2].x < self.temp_tab[0].x < self.temp_tab[1].x < self.temp_tab[3].x and self.temp_tab[0].y < self.temp_tab[3].y < self.temp_tab[1].y < self.temp_tab[2].y:
                self.zamiana_2()
                continue
            elif self.temp_tab[3].x < self.temp_tab[0].x < self.temp_tab[1].x < self.temp_tab[2].x and self.temp_tab[0].y < self.temp_tab[1].y < self.temp_tab[2].y < self.temp_tab[3].y:
                self.zamiana_2()
                continue
            elif self.temp_tab[0].x < self.temp_tab[1].x < self.temp_tab[2].x < self.temp_tab[3].x and self.temp_tab[2].y < self.temp_tab[0].y < self.temp_tab[1].y < self.temp_tab[3].y:
                self.zamiana_2()
                continue
            elif self.temp_tab[0].x < self.temp_tab[1].x < self.temp_tab[2].x < self.temp_tab[3].x and self.temp_tab[2].y < self.temp_tab[0].y < self.temp_tab[3].y < self.temp_tab[1].y:
                self.zamiana_2()
                continue
            elif self.temp_tab[0].x < self.temp_tab[1].x < self.temp_tab[3].x < self.temp_tab[2].x and self.temp_tab[2].y < self.temp_tab[0].y < self.temp_tab[1].y < self.temp_tab[3].y:
                self.zamiana_2()
                continue
            elif self.temp_tab[0].x < self.temp_tab[1].x < self.temp_tab[3].x < self.temp_tab[2].x and self.temp_tab[2].y < self.temp_tab[3].y < self.temp_tab[0].y < self.temp_tab[1].y:
                self.zamiana_2()
                continue
            elif self.temp_tab[0].x < self.temp_tab[3].x < self.temp_tab[1].x < self.temp_tab[2].x and self.temp_tab[2].y < self.temp_tab[3].y < self.temp_tab[0].y < self.temp_tab[1].y:
                self.zamiana_2()
                continue
            elif self.temp_tab[0].x < self.temp_tab[1].x < self.temp_tab[3].x < self.temp_tab[2].x and self.temp_tab[3].y < self.temp_tab[1].y < self.temp_tab[0].y < self.temp_tab[2].y:
                self.zamiana_2()
                continue
            elif self.temp_tab[0].x < self.temp_tab[2].x < self.temp_tab[1].x < self.temp_tab[3].x and self.temp_tab[3].y < self.temp_tab[2].y < self.temp_tab[0].y < self.temp_tab[1].y:
                self.zamiana_2()
                continue
            elif self.temp_tab[1].x < self.temp_tab[0].x < self.temp_tab[2].x < self.temp_tab[3].x and self.temp_tab[3].y < self.temp_tab[1].y < self.temp_tab[0].y < self.temp_tab[2].y:
                self.zamiana_2()
                continue
            elif self.temp_tab[1].x < self.temp_tab[0].x < self.temp_tab[3].x < self.temp_tab[2].x and self.temp_tab[3].y < self.temp_tab[0].y < self.temp_tab[2].y < self.temp_tab[1].y:
                self.zamiana_2()
                continue
            elif self.temp_tab[1].x < self.temp_tab[2].x < self.temp_tab[0].x < self.temp_tab[3].x and self.temp_tab[3].y < self.temp_tab[0].y < self.temp_tab[1].y < self.temp_tab[2].y:
                self.zamiana_2()
                continue
            elif self.temp_tab[2].x < self.temp_tab[1].x < self.temp_tab[3].x < self.temp_tab[0].x and self.temp_tab[3].y < self.temp_tab[2].y < self.temp_tab[1].y < self.temp_tab[0].y:
                self.zamiana_2()
                continue
            #elif self.if_wykluczenie(0,1,2,3,0,1,2,3) == True:
                #continue
            else:
                flaga = 1

    def zamiana(self):
        if self.temp_tab[2].y < self.temp_tab[3].y:
            self.temp_tab[2], self.temp_tab[3] = self.temp_tab[3], self.temp_tab[2]
        if self.temp_tab[1].x > self.temp_tab[3].x:
            self.temp_tab[1], self.temp_tab[3] = self.temp_tab[3], self.temp_tab[1]

    def odleglosci(self,liczba_plt):

        tab = []
        for l in range(len(self.copy_tab_p)):
            tab.append(round(math.sqrt((self.copy_tab_p[l].x - 0) ** 2 + (self.copy_tab_p[l].y - 0) ** 2), 0))

        self.wyszukanie(tab)

        tab = []
        for l in range(len(self.copy_tab_p)):
            tab.append(round(math.sqrt((self.copy_tab_p[l].x - 0) ** 2 + (self.copy_tab_p[l].y - 10) ** 2), 0))

        self.wyszukanie(tab)

        tab = []
        for l in range(len(self.copy_tab_p)):
            tab.append(round(math.sqrt((self.copy_tab_p[l].x - 10) ** 2 + (self.copy_tab_p[l].y - 10) ** 2), 0))

        self.wyszukanie(tab)

        tab = []
        for l in range(len(self.copy_tab_p)):
            tab.append(round(math.sqrt((self.copy_tab_p[l].x - 10) ** 2 + (self.copy_tab_p[l].y - 0) ** 2), 0))

        self.wyszukanie(tab)

        self.wykluczenie()

        #self.zamiana_x()
        #self.zamiana()
        #self.zamiana()
        #self.zamiana()
        #self.zamiana()

        x = [self.temp_tab[0].x, self.temp_tab[1].x, self.temp_tab[2].x, self.temp_tab[3].x, self.temp_tab[0].x]
        y = [self.temp_tab[0].y, self.temp_tab[1].y, self.temp_tab[2].y, self.temp_tab[3].y, self.temp_tab[0].y]

        x1 = [self.temp_tab[0].x]
        y1 = [self.temp_tab[0].y]

        x2 = [self.temp_tab[1].x]
        y2 = [self.temp_tab[1].y]

        x3 = [self.temp_tab[2].x]
        y3 = [self.temp_tab[2].y]

        x4 = [self.temp_tab[3].x]
        y4 = [self.temp_tab[3].y]


        plt.subplot(5,5,liczba_plt+1)
        plt.plot(x, y)
        plt.plot(x1, y1, 'o')
        plt.plot(x2, y2, '*')
        plt.plot(x3, y3, 's')
        plt.plot(x4, y4, 'd')
        plt.grid()
"""


#ABC = Trojkat()
#ABC1 = Trojkat()
#ABC.draw()
#ABC1.draw()
#ABC.drawShow()
"""
for i in range(24):
    ABCD = Prostokat()
    ABCD.wyszukanie_2(i)
    ABCD.draw(i)
"""

#ABCD = Prostokat(10)
#print("Pole:",ABCD.pole())
#print("Obwód:",ABCD.obwod())
for i in range(25):
    ABCD = Prostokat(10)
    ABCD.draw(i)
ABCD.drawShow()

#ABCD = Prostokat()
#ABCD.draw()
#plt.show()

#ABCD.draw()
#ABCD.drawShow()

#print("ABC")
#print("Obwód: ",ABC.obwod(),"\nPole: ",ABC.pole())

#print("ABCD")
#print("Obwód: ",ABCD.obwod(),"\nPole: ",ABCD.pole())

#print("ABCD")
#print("Obwód: ",ABCD.obwod(),"\nPole: ",ABCD.pole())