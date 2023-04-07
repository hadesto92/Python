#Matura 2018

#Karol Lach

#Podaj liczbę wierszy w pliku slowa.txt, w których występują pary słów takich, że pierwsze słowo jest anagramem drugiego.
# Wypisz te pary.

#Wczytanie pliku do zmiennej
file_temp = open("slowa.txt", "r")
content = file_temp.read()
content_temp = content.split("\n")

#Zliczenie wierszy
content_len = len(content.split("\n"))

#Zapisanie słów do listy
tab_word = []
sign_temp = ''

for line in content_temp:
    if line == '':
        break
    two_word = []
    word = ''
    for sign in line:
        if sign == ' ' or sign == '\n':
            two_word.append(word)
            word = ''
        else:
            word+=sign
    two_word.append(word)
    tab_word.append(two_word)

#Posortowanie słów i sprawdzenie czy są takie same jeśli tak wypisz je

counter=0

for line in tab_word:
    temp_line0 = ''.join(sorted(line[0]))
    temp_line1 = ''.join(sorted(line[1]))

    if(temp_line0==temp_line1):
        print(line)
        counter+=1

print("Liczba wierszy z anagramami: "+str(counter))
