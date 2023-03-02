#Matura 2018

#Karol Lach

#W tym zadaniu rozważmy odległość liter w alfabecie - np. litery A i B są od siebie oddalone o 1, A i E o 4, F i D o 2,
# a każda litera od siebie samej jest oddalona o 0. Wypisz wszystkie słowa, w których każde dwie litery oddalone są od
# siebie w alfabecie co najwyużej o 10. Słowa wypisz w kolejności występowania w pliku sygnaly.txt, po jednym w wierszy.

#Odczytanie pliku i zapisanie do zmiennej
file_temp = open("sygnaly.txt", "r")
file_save = open("result.txt", "a")
content = file_temp.read()
content_temp = content.split("\n")

#Pierwsza pętla wybierająca wiersz
for number_line in range(0, len(content_temp)):
    flag = 'true'
    #Druga pętla sprawdzająca litery każdą z każdą jeśli wynik będzie więszy od 10 lub mniejszy od -10 ustawia flagę na false i czeka na kolejną pętlę
    #Akceptowane odległości <-10, 10>
    for sign in range(0, len(content_temp[number_line])):
        line = content_temp[number_line]
        for sign_temp in range(sign+1, len(content_temp[number_line])):
            if(ord(line[sign])-ord(line[sign_temp])<-10 or ord(line[sign])-ord(line[sign_temp])>10):
                flag = 'false'
        if flag == 'false':
            break

    #Zapisanie odpowiedzi w pliku i zamknięcie plików
    if flag == 'true':
        print(content_temp[number_line])
        file_save.write(str(content_temp[number_line])+"\n")


#Zamknięcie plików
file_save.close()
file_temp.close()


