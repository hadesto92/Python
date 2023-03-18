#Matura 2018

#Karol Lach

#Podaj liczbę wierszy z pliku slowa.txt zawierających pary słów, w których pierwsze słowo zawiera się w drugim słowie.

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

#Zliczenie wierszy
counter = 0

for line in tab_word:
    if line[0] in line[1]:
        counter+=1

print(counter)

