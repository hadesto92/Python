#Matura 2015

#Karol Lach

#Znajdź najmniejszą i największą liczbę w pliku liczby.txt. Jako odpowiedź podaj numery wierszy, w których się one znajdują.

#Wczytanie pliku do zmiennej
file_temp = open("liczby.txt", "r")
content = file_temp.read()
content_temp = content.split("\n")

#Zliczenie wierszy
content_len = len(content_temp)
MIN_result = 0
MAX_result = 0
MIN_result_number_line = 0
MAX_result_number_line = 0

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

    #Pierwsza pętla przypisanie wyników do MIN i MAX
    if(number_line == 0):
        MIN_result = result
        MAX_result = result
        MIN_result_number_line = number_line
        MAX_result_number_line = number_line

    #Klejne pętle sprawdzenie czy wynik jest mniejszy od poprzednika lub większy od poprzednika
    if(MIN_result > result):
        MIN_result = result
        MIN_result_number_line = number_line
    if(MAX_result < result):
        MAX_result = result
        MAX_result_number_line = number_line

print("Minimalna: "+str(MIN_result)+" linijka: "+str(MIN_result_number_line+1))
print("Maksymalna: "+str(MAX_result)+" linijka: "+str(MAX_result_number_line+1))