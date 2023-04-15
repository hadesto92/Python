#Matura 2020

#Karol Lach

#Dla każdego słowa z pliku pary.txt znajdź długośc najdłuższego spójnego fragmentu tego słowa złożonego z identycznych liter.
# Wypisz znalezione fragmenty słów i ich długość oddzielone spacją, po jednej parze w każdym wierszu. Jeżeli istnieją dwa fragmenty
# o takiej samej największej długości, podaj pierwszy z nich. Wyniki podaj w kolejnośći zgodnej z kolejnością danych w pliku pary.txt.

#Wczytanie pliku do zmiennej
file_temp = open("pary.txt", "r")
content = file_temp.read()
content_temp = content.split("\n")

#Zapisanie wczytanego pliku do listy
tab_pair = []
for line in content_temp:
    tab_temp = []
    temp_sing=''
    for sign in line:
        if sign!=' ':
            temp_sing+=sign
        else:
            tab_temp.append(temp_sing)
            temp_sing = ''
    tab_temp.append(temp_sing)
    tab_pair.append(tab_temp)

#print(tab_pair)

index = 0
for line in tab_pair:
    counter = 0
    temp_counter = 0
    temp_sign = ''
    sign = ''
    result_sign = ''
    for sign_index in line[1]:
        if(index == 0):
            temp_sign = sign_index
            sign = sign_index
            temp_counter = 1
        else:
            if(sign_index == temp_sign):
                temp_counter+=1
                sign+=sign_index
            else:
                if(counter<=temp_counter):
                    result_sign=sign
                    counter=temp_counter
                temp_sign = sign_index
                sign = sign_index
                temp_counter = 1
    if (counter > 1):
        print(result_sign, counter)

    index += 1
    if (index == len(tab_pair)-1):
        break
