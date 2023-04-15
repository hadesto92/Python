#Matura 2020

#Karol Lach

#Krotnością luki nazywamy liczbę jej wystąpień. Najczęstszą luką nazywamy lukę o największej krotności. Podaj krotność
# najczęstrzej luki oraz wartość wszystkich najczęstrzych luk w ciągu z pliku dane4.txt.

#Wczytanie pliku do zmiennej
file_temp = open("dane4.txt", "r")
content = file_temp.read()
content_temp = content.split("\n")

#Zapisanie liczb do listy
number_list = []

for line in content_temp:
    if line == '':
        break
    number_list.append(int(line))

#Sprawdzenie i zapisanie luk w tablicy wraz z ich występowaniem
tab_gap = []
for index in range(len(number_list)-1):
    gap = abs(number_list[index] - number_list[index + 1])
    if(index == 0):
        temp_tab = []
        temp_tab.append(gap)
        temp_tab.append(1)
        tab_gap.append(temp_tab)
    else:
        flage=False
        for index_2 in range(len(tab_gap)-1):
            if tab_gap[index_2][0] == gap:
                tab_gap[index_2][1]+=1
                flage=True
            else:
                flage=False
        if flage == False:
            temp_tab = []
            temp_tab.append(gap)
            temp_tab.append(1)
            tab_gap.append(temp_tab)

#Znalezienie najczęściej występującej luki
max_gap_index = 0
for index in range(len(tab_gap)-1):
    if(tab_gap[index][1]>max_gap_index):
        max_gap_index = tab_gap[index][1]

#Wypisanie wszystkich wartości luk które najczęściej wystepują
for index in range(len(tab_gap)-1):
    if(tab_gap[index][1]==max_gap_index):
        print(tab_gap[index][0], tab_gap[index][1])