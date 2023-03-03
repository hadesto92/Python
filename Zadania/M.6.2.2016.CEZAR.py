#Matura 2016

#Karol Lach

#W pliku dane_6_2.txt zapisano 3000 szyfrogramów i odpowiadające im klucze szyfrujące. W każdym wierszu znajduje się
# jeden szyfrogram i po pojedyńczym znaku odstępu odpowiadający mu klucz. Napisz program który odszyfruje słowa zaszyfrowane
# podanymi kluczami. Wynik zapisz w pliku wynik_6_2.txt: każde odszyfrowane słowo w osobnym wierszu, w porządu odpowiadającym
# kolejności szyfrogramów z plików z danymi.


#Wczytanie pliku do zmiennej
file_temp = open("dane_6_2.txt", "r") #Otwarcie pliku w formie do odczytu
file_save = open("wyniki_6_2.txt", "a") #Otwarcie pliku w formie do zapisu (dopisuje na końcu pliku)
content = file_temp.read()
content_temp = content.split("\n")

#Zliczenie wierszy
content_len = len(content_temp)

#Pierwsza pętla przechodząca przez wiersze
for number_line in range(0,content_len):

    index_temp = 0
    key = '0'
    result = ''

    #Sprawdzenie w którym miejscu znajduje się biały znak
    for number_sign in range(0, len(content_temp[number_line])):
        line = content_temp[number_line]
        if(line[number_sign] == ' '):
            index_temp = number_sign
            break

    #Pobranie za pomocą pętli klucza znajdującego się za białym znakiem
    for number_sign in range(index_temp+1, len(content_temp[number_line])):
        line = content_temp[number_line]
        key+=line[number_sign]

    key = int(key) #Utworzenie klucza i zamiana typu ze str na int

    #Znalezienie odpowiedniego klucza
    while key > 26:
        key -= 26

    #Druga pętla przechodząca przez litery w wierszu i deszyfrująca je przy odpowiednim kluczu
    for number_sign in range(0, index_temp):
        line = content_temp[number_line] #Utworzenie zmiennej która trzyma nam dany wiersz jako jedną wartość
        if(ord(line[number_sign])-key>=65):
            result += chr(ord(line[number_sign])-key)
        else:
            result += chr((ord(line[number_sign])-key)+26)

    #Zapisanie wyniku do pliku
    file_save.write(result + "\n")

#Zamknięcie plików
file_save.close()
file_temp.close()