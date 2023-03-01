#Matura 2018

#Karol Lach

#Znajdź słowo, w którym występuje największa liczba różnych liter. Wypisz to słowo i liczbnę występujhących w nim różnych liter.
# Jeśli słów o największej liczbie różnych liter jest więcej niż jedno, wypisz pierwsze z nich pojawiające się w pliku z danymi.


#Odczytanie pliku i zapisanie do zmiennej
file_temp = open("sygnaly.txt", "r")
content = file_temp.read()
content_temp = content.split("\n")

#Zliczenie wierszy
content_len = len(content.split("\n"))

#Utworzenie tablicy wyników gdzie będą trzymana liczba znaków w wierszu bez powtórzeń
result = []

#Utworzenie pętli którą będzie szła przez każdy wiersz
for i in range(0,content_len):

    #Usunięcie potarzających się liter z wiersza i zliczenie długości zapisanie do tablicy
    result.append(len(set(content_temp[i])))

#Sprawdzenie tablicy i wypisanie pierwszego najwyższego wyniku
conter = 0
for j in range(0,content_len):
    if result[j] == max(result):
        print('STOP')
        conter = j
        break

print(conter)
print(result[conter])
print(content_temp[conter])

#Zapisanie odpowiedzi w pliku i zamknięcie plików
file_save = open("result.txt", "a")
file_save.write(str(content_temp[conter])+" "+str(result[conter])+"\n")

file_save.close()
file_temp.close()
