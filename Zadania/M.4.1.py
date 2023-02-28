#Matura 2018

#Karol Lach

#Naukowcy zauważyli, że po złączeniu dziesiątych liter co czterdziestego słowa otrzymamy pewne przesłanie. Wypisz to przesłanie.

#Wczytanie pliku do zmiennej
file_temp = open("sygnaly.txt", "r")
content = file_temp.read()

#Zliczenie wierszy
content_len = len(content.split("\n"))

#Utworzenie pierwszej pętli wybierającej wiersz
content_temp = content.split("\n")

result = ''

for i in range(39, content_len, 40):
    if(len(content_temp[i])>=10):

        #Utworzenie drugiej pętli wybierającej literę w wierszu jeśli posiada 10 lub więcej liter
        conter = 0
        conter2 = 10
        for j in content_temp[i]:
            conter += 1

            # Przypisanie litery do zmiennej (nadpisanie)
            if conter == conter2:
                result = result+j
                break

#Zakończenie pętli i wypisanie słowa
print(result)

#Zapisanie odpowiedzi w pliku i zamknięcie plików
file_save = open("result.txt", "a")
file_save.write(result+"\n")

file_save.close()
file_temp.close()

