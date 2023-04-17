#Matura 2018

#Karol Lach

#Napisz program, który utworzy plik wyniki4_4.txt zawierający w kolejnych wierszach ciągi uporządkowane, będące wynikiem
# scalenia odpowiadających im co do kolejności ciągów z plików dane1.txt i dane2.txt. Liczby w ciągach wynikowych zapisz
# rozdzielając je spacjami.

#Wczytanie plików do zmiennych
file_temp = open("dane1.txt", "r")
content = file_temp.read()
content_temp = content.split("\n")

file_temp2 = open("dane2.txt", "r")
content2 = file_temp2.read()
content_temp2 = content2.split("\n")



#Tworzę dwie listy każda dla odzielnych danych gdzie każda linijka jest odzielną wartością dla listy
data1 = []
for line in content_temp:
    if line == '':
        break
    sign_temp = ''
    temp_data1 = []
    for sign in line:
        if(sign != ' '):
            sign_temp+=sign
        else:
            temp_data1.append(sign_temp)
            sign_temp=''
    temp_data1.append(sign_temp)
    data1.append(temp_data1)

#print(data1)

data2 = []
for line2 in content_temp2:
    if line2 == '':
        break
    sign_temp2 = ''
    temp_data2 = []
    for sign2 in line2:
        if(sign2 != ' '):
            sign_temp2+=sign2
        else:
            temp_data2.append(sign_temp2)
            sign_temp2=''
    temp_data2.append(sign_temp2)
    data2.append(temp_data2)

#print(data2)

#Zapisanie obu list do jednej linijka po linijce od razu sortując zawartość
tab_result = []
lenth = int((len(data1)+len(data2))/2)
for index in range(lenth):
    result = []
    lenth2 = int((len(data1[index]) + len(data2[index])) / 2)
    for index2 in range(lenth2):
        result.append(int(data1[index][index2]))
        result.append(int(data2[index][index2]))
    tab_result.append(sorted(result))
#print(tab_result)

#Zapisanie odpowiedzi do pliku
file_save = open("wyniki4_4.txt", "a")

for line in tab_result:
    result=''
    for sign in line:
        result+=str(sign)+' '
    file_save.write(result+"\n")

file_save.close()