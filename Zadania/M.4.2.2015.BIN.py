#Matura 2015

#Karol Lach

#Podaj, ile liczb w pliku liczby.txt jest podzielnych przez 2 oraz ile liczb jest podzielnych przez 8

#Wczytanie pliku do zmiennej
file_temp = open("liczby.txt", "r")
content = file_temp.read()
content_temp = content.split("\n")

#Zliczenie wierszy
content_len = len(content_temp)

two = 0
eight = 0

#Pierwsza pętla przechodząca przez wiersze
for number_line in range(0,content_len):
    tracker = 0
    result = 0

    #Druga pętla przerabiająca system BIN na DEC
    for number_sign in range(len(content_temp[number_line])-1, -1, -1):
        line = content_temp[number_line]
        if line[number_sign] == '1':
            result += pow(2, tracker)
        tracker+=1
    #Sprawdzenie czy wynik jest podzielny przez 2 lub 8 i zliczenie ilości razy
    if result%2 == 0:
        two += 1
    if result%8 == 0:
        eight += 1

print("Przez dwa: "+str(two))
print("Przez osiem: "+str(eight))
