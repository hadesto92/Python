#Matura 2020

#Karol Lach

#Fragment ciągu nazywamy regularnym, jeśli wszystkie jego luki mają tę samą wartość. Znajdź najdłuższy fragment regularny
# w ciągu z pliku dane4.txt. Podaj jego długość oraz wartości (liczby) znajdujące się na początku i końcu tego fragmentu.
# W pliku z danymi jest jeden taki fragment.

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

#Zapisanie wszystkich luk do tabeli wraz z początkowym indexem, wielością luki i długością ciągu luki
max_len = 0
max_gap = 0
first_index = 0
tab_result = []
for index in range(len(number_list)-1):
    result = abs(number_list[index] - number_list[index + 1])
    if(index == 0):
        max_len = 1
        max_gap = result
        first_index = index
    else:
        if(result == max_gap):
            max_len+=1
        else:
            tab_temp = []
            tab_temp.append(max_len)
            tab_temp.append(max_gap)
            tab_temp.append(first_index)
            tab_result.append(tab_temp)

            max_len = 1
            max_gap = result
            first_index = index

#Znalezienie najdłuższego ciągu
max_len = 0
index_range = 0
for index in range(len(tab_result)-1):
    if(max_len<tab_result[index][0]):
        max_len = tab_result[index][0]
        index_range = index

#Wypisanie długości ciągu, pierwszej liczby i ostatniej liczby
print(tab_result[index_range][0], number_list[tab_result[index_range][2]], number_list[tab_result[index_range][2]+tab_result[index_range][0]])
