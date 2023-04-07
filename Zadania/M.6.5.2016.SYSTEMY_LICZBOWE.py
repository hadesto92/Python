#Matura 2016

#Karol Lach

#Podaj kod najiekszej oraz kod najmniejszej spośród liczb zakodowanych w pliku liczby2.txt oraz ich wartość w systemie dziesiętnym.

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

#Przeliczenie wszystkich liczb na dziesiętny i dodanie ich do nowej tablicy
counter_tab = []
counter = 0

for line in tab_word:
    three_word = []
    three_word.append(int(line[0],int(line[1])))
    three_word.append(line[0])
    three_word.append(line[1])
    counter_tab.append(three_word)

#print(counter_tab)

#Sprwadzenie która liczba jest najmniejsza, a która największa
temp_min = counter_tab[0]
temp_max = counter_tab[0]

for line in counter_tab:
    if line[0] < temp_min[0]:
        temp_min = line
    if line[0] > temp_max[0]:
        temp_max = line

print('Najmniejsza licza: '+str(temp_min[0])+' dla liczby: '+str(temp_min[1])+' z systemu: '+str(temp_min[2]))
print('Największa licza: '+str(temp_max[0])+' dla liczby: '+str(temp_max[1])+' z systemu: '+str(temp_max[2]))