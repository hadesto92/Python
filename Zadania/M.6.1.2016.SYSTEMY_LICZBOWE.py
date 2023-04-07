#Matura 2016

#Karol Lach

#Podaj, ile liczb w pliku liczby2.txt zapisano w systemie ósemkowym.

#Wczytanie pliku do zmiennej
file_temp = open("liczby2.txt", "r")
content = file_temp.read()
content_temp = content.split("\n")

#Zliczenie wierszy
content_len = len(content.split("\n"))

#Zapisanie numerów do listy dwuwymiarowej z oznaczeniem systemu
tab_word = []
sign_temp = ''

for line in content_temp:
    counter=0
    if line == '':
        break
    two_word = []
    word = ''

    for sign in line:
        counter+=1
        if counter < len(line):
            word+=sign
        else:
            two_word.append(word)
            two_word.append(sign)

    tab_word.append(two_word)

#Zliczenie ile liczb zapisano w systemie ósemkowym

counter = 0

for line in tab_word:
    if line[1] == '8':
        #print(line)
        counter+=1

print(counter)
