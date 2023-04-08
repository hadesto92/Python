#Matura 2019

#Karol Lach

#Podaj, ile z podanych liczb jest potęgami liczby 3.

#Wczytanie pliku do zmiennej
file_temp = open("liczby3.txt", "r")
content = file_temp.read()
content_temp = content.split("\n")

#Zliczenie wierszy
content_len = len(content.split("\n"))

#Zapisanie liczb do listy
number_list = []

for line in content_temp:
    if line == '':
        break
    number_list.append(int(line))

#print(number_list)

#Sprawdzenie który element z listy jest podzielny przez 3 bez reszty aż do osiągnięcia 1 wtedy to jest pożądana liczba
counter=0
for number in number_list:
    counter_number = number
    #print("First"+str(counter_number))
    while counter_number>0:
        #print(counter_number)
        if counter_number%3 == 0:
            counter_number = counter_number/3
            #print(counter_number)
            if counter_number == 1:
                counter+=1
        else:
            break
print(counter)