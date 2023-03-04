#Matura 2016

#Karol Lach

#W piku dane_6_3.txt zapisano 3000 par słów, po jednej parze w wierszu, oddzielonych pojednyńczym znakiem odstępu.
# Drugie słowo w każdej parze jest szyfrogramem pierwszego z nieznanym kluczem. Niektóre szyfrogramy są błędne, co
# oznacza, że niektóre litery w słowie zakodowano z różnymi przesunięciami. Słowo ma zawsze tę samą długość co
# odpowiadający mu szyfrogram. Napisz program, który wyszuka i wypisze te słowa z pliku dane_6_3.txt, które błędnie
# zaszyfrowano. Wynik zapisz w pliku wyniki_6_3.txt: każde słowo w osobnym wierszu, w porządku odpowiadającym kolejności
# tych słów z pliku z danymi.


#Wczytanie pliku do zmiennej
file_temp = open("dane_6_3.txt", "r") #Otwarcie pliku w formie do odczytu
file_save = open("wyniki_6_3.txt", "a") #Otwarcie pliku w formie do zapisu (dopisuje na końcu pliku)
content = file_temp.read()
content_temp = content.split("\n")

#Zliczenie wierszy
content_len = len(content_temp)

#Pierwsza pętla przechodząca przez wiersze
for number_line in range(0,content_len-1):

    index_temp = 0
    key = 0
    result = ''
    temp_cipher = ''
    line = content_temp[number_line]

    #Sprawdzenie w którym miejscu znajduje się biały znak
    for number_sign in range(0, len(content_temp[number_line])):
        if(line[number_sign] == ' '):
            index_temp = number_sign
            break

    #Utworzenie klucza dla danego wiersza za pomocą pierwszego znaku słowa i pierwszego znaku szyfrogramu
    first_sign_in_word = line[0]
    first_sign_in_cipher = line[index_temp+1]
    key = ord(first_sign_in_cipher) - ord(first_sign_in_word)

    if(key<0):
        key+=26
    if(key>26):
        key-=26

    #Zapisanie do zmiennej tymczasowej szyfrogramu z pliku
    for number_sign in range(index_temp+1, len(content_temp[number_line])):
        temp_cipher+=line[number_sign]

    #Zamienienie słowa na szyfrogram za pomocą klucz
    for number_sign in range(0, index_temp):
        if(ord(line[number_sign])+key<=90):
            result += chr(ord(line[number_sign])+key)
        else:
            result += chr((ord(line[number_sign])+key)-26)

    #Porównanie obu szyfrogramów jeśli nie zgadzają się to zapisujemy je do pliku
    if(temp_cipher!=result):
        temp_word = ''
        for number_sign in range(0, index_temp):
            temp_word += line[number_sign]
        file_save.write(temp_word + "\n")
        print(temp_word)


#Zamknięcie plików
file_save.close()
file_temp.close()