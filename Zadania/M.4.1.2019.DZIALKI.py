#Matura 2019

#Karol Lach

#W pliku działki.txt zapisano 50 map działek przeznaczonych na sprzedaż. Każda działka ma kształt kwadratu o boku 30 jednostek
# i jest podzielona na 30x30 jednostkowych kwadratowych pól. Mapa zawiera 30 wierszy, z których każdy ma po 30 znaków opisujących
# pola. Po każdej mapie jest jeden pusty wiersz. Znak . oznacza, że odpowiednie pole jest puste, znak * oznacza fragment
# działki porośnięty trawą, a znak X - przeszkodę terenową.

#Oblicz, ile jest działek, w których co najmniej 70% powierzchni jest porośnięte trawą.

#Wczytanie pliku do zmiennej
file_temp = open("dzialki.txt", "r")
content = file_temp.read()
content_temp = content.split("\n")

#Zliczenie wierszy
content_len = len(content.split("\n"))
flag = 0
counter = 0         #Zmienna zliczająca liczbę działek które mają więcej niż 70% trawy
counter_grass = 0   #Jeśli działka posiada powieżchnię 30x30 czyli razem jest 900 znaków to znaczy że trawa powinna
                    # rosnąć w przedziale <630, 900>

#Pierwsza pętla, która będzie przechodziła przez wiersze
for number_line in range(0,content_len):
    line = content_temp[number_line]

    if(flag<30):
        #Druga pętla która będzie obliczała ile jest znaków * w wierszach resetując się co 31 wierszy
        for number_sign in range(0, len(content_temp[number_line])):
            if line[number_sign] == '*':
                counter_grass+=1
        flag += 1

    else:

        if counter_grass >= 630:
            counter+=1

        counter_grass = 0
        flag = 0


print("Liczba działek gdzie trawa rośnie na 70% powieżchni: "+str(counter))