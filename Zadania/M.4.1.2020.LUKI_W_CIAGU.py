#Matura 2020

#Karol Lach

#Podaj wartość największej luki oraz wartość najmniejszej luki pomiędzy elementami ciągu z pliku dane4.txt.

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

#print(number_list)

#Sprawdzenie każdej liczby w ciągu i porównanie jej do następnika oraz wyszukanie najmniejszej lub największej luki
list_gap = []
max_gap = 0
min_gap = 0

for index in range(len(number_list)-1):
    result = abs(number_list[index]-number_list[index+1])
    #print(result)
    if index == 0:
        min_gap = result
        max_gap = result
    else:
        if result>max_gap:
            max_gap = result
        if result<min_gap:
            min_gap=result

    list_gap.append(max_gap)
    list_gap.append(min_gap)

#print(list_gap)
print(min(list_gap))
print(max(list_gap))