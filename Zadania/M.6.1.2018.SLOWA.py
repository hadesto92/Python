#Matura 2018

#Karol Lach

#Podaj, ile słów w pliku slowa.txt kończy się na literę A

#Wczytanie pliku do zmiennej
file_temp = open("slowa.txt", "r")
content = file_temp.read()
content_temp = content.split("\n")

#Zliczenie wierszy
content_len = len(content.split("\n"))

#Zapisanie słów do listy
tab_word = []
sign_temp = ''

for sign in content:
    if(sign != ' ' and sign != '\n'):
        sign_temp+=sign
    else:
        tab_word.append(sign_temp)
        sign_temp=''

#Sprawdzenie które słowa kończą się na A i podniesienie licznika słów
counter = 0

for sign in tab_word:
    for number_sign in range(len(sign)):
        if number_sign == len(sign)-1:
            if(sign[number_sign] == 'A'):
                counter+=1

print(counter)

#Drugie rozwiązanie
counter = 0
for sign in tab_word:
    if sign[-1] == 'A':
        counter+=1

print(counter)