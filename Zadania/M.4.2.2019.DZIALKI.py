#Matura 2019

#Karol Lach

#W pliku działki.txt zapisano 50 map działek przeznaczonych na sprzedaż. Każda działka ma kształt kwadratu o boku 30 jednostek
# i jest podzielona na 30x30 jednostkowych kwadratowych pól. Mapa zawiera 30 wierszy, z których każdy ma po 30 znaków opisujących
# pola. Po każdej mapie jest jeden pusty wiersz. Znak . oznacza, że odpowiednie pole jest puste, znak * oznacza fragment
# działki porośnięty trawą, a znak X - przeszkodę terenową.

#Po analizie map okazało się, że dwie działki, których mapy po obróceniu jednej z nich o 180stopni są identyczne. Podaj numery tych działek.

#Wczytanie pliku do zmiennej
file_temp = open("dzialki.txt", "r")
content = file_temp.read()
content_temp = content.split("\n")

#Zliczenie wierszy
content_len = len(content.split("\n"))

#Zapisanie dzialek do listy dwuwymiarowej
tab_plot = []
flag = 0

while True:
    if(flag == content_len):
        break

    temp_line = []

    for number_line in range(flag,flag+30):
        temp_line.append(content_temp[number_line])

    tab_plot.append(temp_line)

    flag+=31

#Utworzenie drógiej listy i odwrócenie każdej działki o 180 stopni
tab_plot2 = []

#temp=tab_plot[1][1]
#print(tab_plot[1][1])
#print(temp[::-1])

for plot in tab_plot:

    temp_line = []
    for number_line_plot in range(len(plot)-1,-1,-1): #przejście przez listę od końca do początku należy pamiętać że druga wartość do wartość do której dąży ale jej nie "osiągnie"
        temp_line_plot = plot[number_line_plot]
        temp_line.append(temp_line_plot[::-1]) #Odwrócenie stringa o 180 stopni
    tab_plot2.append(temp_line)

#Sprawdzenie czy działki są sobie równe po odwórceniu i wypisanie wyniku jeśli są jakieś równe
for index_plot in range(len(tab_plot)):
    for index_plot2 in range(len(tab_plot2)):
        if tab_plot[index_plot]==tab_plot2[index_plot2]:
            print("Są równe: "+str(index_plot)+" "+str(index_plot2))
