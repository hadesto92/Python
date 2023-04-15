#Matura 2020

#Karol Lach

#Rozważ wszystkie pary (liczba, słowo) zapisane w wierszach pliku pary.txt, dla których liczba jest równa długości słowa,
# i wypisz spośród nich taką parę, która jest mniejsza od wszystkich pozostałych. W pliku pary.txt jest jedna taka para.

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

#Znalezienie słów równych liczbie
index = 0
number_line = 0
sign_line = ''
flage = False
for line in tab_pair:
    if(int(line[0])==len(line[1])):
        if(flage == False): #Jeśli jest to pierwsze równe słowo liczbie
            number_line = int(line[0])
            sign_line = line[1]
            flage = True
        else:
            if(int(line[0])<number_line or (int(line[0])==number_line and line[1]<sign_line)): #Sprawdzenie warunków mniejszości słów i liczb
                number_line = int(line[0])
                sign_line = line[1]

    index += 1
    if (index == len(tab_pair) - 1):
        break

print(number_line, sign_line)