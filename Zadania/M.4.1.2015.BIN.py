#Matura 2015

#Karol Lach

#Podaj ile liczb z pliku liczby.txt ma w swoim zapisie binarnym więcej zer niż jedynek

#Wczytanie pliku do zmiennej
file_temp = open("liczby.txt", "r")
content = file_temp.read()
content_temp = content.split("\n")

#Zliczenie wierszy
content_len = len(content_temp)

#Przygotowanie danych wyjściowych
result = 0

#Pierwsza pętla przechodząca przez wiersze
for number_line in range(0,content_len):

    zero = 0
    one = 0

    #Druga pętla zliczająca zera i jedynki w wierszach
    for number_sign in range(0, len(content_temp[number_line])):
        line = content_temp[number_line]
        if line[number_sign] == '0':
            zero+=1
        else:
            one+=1

    #Porównanie wyników i podjęcie decyzji
    if zero>one:
        result+=1

#Wypisanie wyniku
print(result)