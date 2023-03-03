#Matura 2016

#Karol Lach

#W pliku dane_6_1.txt znajduje się 100 słów. Słowa umieszczono w osobnych wierszach. Napisz program który zaszyfruje
# słowa (SZYFR CEZARA) w pliku dane_6_1.txt z użyciem klucza k=107. Wynik zapisz do pliku wyniki_6_1.txt,
# każde słowo w osobnym wierszu, w porządu odpowiedającym kolejności słów z pliku z danymi.

#Wczytanie pliku do zmiennej
file_temp = open("dane_6_1.txt", "r") #Otwarcie pliku w formie do odczytu
file_save = open("wyniki_6_1.txt", "a") #Otwarcie pliku w formie do zapisu (dopisuje na końcu pliku)
content = file_temp.read()
content_temp = content.split("\n")

#Zliczenie wierszy
content_len = len(content_temp)

#Przeliczenie klucza. W zadaniu należy przeliczyć klucz aby zmieniał litery od A do Z czyli od 65 do 90 różnica wychodzi
# 26 czyli zmiejszamy każdy klucz o 26 do puki nie będzie mniejszy niż 26 dopiero ta wartość staje się naszym kluczem
klucz = 107

while klucz>26:
    klucz-=26

#Pierwsza pętla przechodząca przez wiersze
for number_line in range(0,content_len):
    result = ''
    #Druga pętla przechodząca przez litery w wierszu i podmieniająca je na odpowiednie litery z szyfru
    for number_sign in range(0, len(content_temp[number_line])):
        line = content_temp[number_line] #Utworzenie zmiennej która trzyma nam dany wiersz jako jedną wartość
        if(ord(line[number_sign])+klucz<=90):
            result += chr(ord(line[number_sign])+klucz)
        else:
            result += chr((ord(line[number_sign])+klucz)-26)
    #Zapisanie linijki
    file_save.write(result + "\n")

file_save.close()
file_temp.close()