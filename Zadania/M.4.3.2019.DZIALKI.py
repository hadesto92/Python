#Matura 2019

#Karol Lach

#W pliku działki.txt zapisano 50 map działek przeznaczonych na sprzedaż. Każda działka ma kształt kwadratu o boku 30 jednostek
# i jest podzielona na 30x30 jednostkowych kwadratowych pól. Mapa zawiera 30 wierszy, z których każdy ma po 30 znaków opisujących
# pola. Po każdej mapie jest jeden pusty wiersz. Znak . oznacza, że odpowiednie pole jest puste, znak * oznacza fragment
# działki porośnięty trawą, a znak X - przeszkodę terenową.

#W rogu północno-zachdnim działki trzeba wytyczyć kwadratowy plac, który nie może zawirać przeszkód terenowych. Znajdź
# działkę, na której zmieści się taki plac o największej powierzchni. Jako odpowiedź podaj numer tej działki oraz
# długość boku placu. Jeśli jest więcej takich działek, podaj numery ich wszystkich.

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

#Utworzenie pętli która będzie przechodziła przez działki

number_plot = 0

result_plot = []
result_max_side = 0

for plot in tab_plot:
    #print("Działka: "+str(number_plot))
    for counter in range(30):
        temp_counter = counter
        #print("Maksymalny znacznik: "+str(temp_counter))
        flage = True
        for x in range(temp_counter+1):
            #print("Linijka: "+str(temp_counter)+" Kolumna: "+str(x))
            #print(tab_plot[number_plot][temp_counter][x])

            #print("Linijka: " + str(x) + " Kolumna: " + str(temp_counter))
            #print(tab_plot[number_plot][x][temp_counter])

            if tab_plot[number_plot][temp_counter][x] == "X" or tab_plot[number_plot][x][temp_counter] == "X":
                flage = False
                break
        if flage == False:

            if result_max_side <= temp_counter:
                if result_max_side == temp_counter:
                    result_plot.append(number_plot+1)
                else:
                    result_max_side = temp_counter
                    result_plot = []
                    result_plot.append(number_plot+1)

            #print(temp_counter)
            break
    number_plot+=1

print("Numery działki/ek o największej powieżchni: "+str(result_plot)+" o wymiarze pola: "+str(result_max_side)+"m2")
