#Matura 2018

#Karol Lach

#Porównaj ciągi zapisane w odpowiadających sobie wierszach w plikach dane1.txt i dane2.txt. Podaj, w ilu wierszach zapisane
# są ciągi, których ostatnia liczba jest taka sama. Dla danych z plików przyklad1_a. txt oraz przyklad2_a.txt wynikiem jest 3.

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

#Porównanie list i wypisanie ile jest ciągów gdzie ostatnia liczba jest taka sama
counter=0
lenth = int((len(data1)+len(data2))/2)
for index in range(lenth):
    if data1[index][-1] == data2[index][-1]:
        counter+=1

print(counter)