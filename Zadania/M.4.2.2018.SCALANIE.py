#Matura 2018

#Karol Lach

#Podaj, ile jest par ciągów (w odpowiadających sobie wierszach plików dane1.txt i dane2.txt) takich, że w jednym i drugim
# ciągu jest 5 liczb parzystych i 5 liczb nieparzystych. Dla danych z plików przyklad1_a.txt oraz przyklad2_a.txt wynikiem jest 1.

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

#Sprawdzenie czy ciągi mają po 5 liczb parzystych i nieparzystych
counter=0
lenth = int((len(data1)+len(data2))/2)
for index in range(lenth):
    lenth2 = int((len(data1[index])+len(data2[index]))/2)
    counter_odd_1 = 0
    counter_odd_2 = 0
    counter_even_1 = 0
    counter_even_2 = 0

    for index2 in range(lenth2-1):
        if(int(data1[index][index2])%2==0):
            counter_even_1+=1
        else:
            counter_odd_1+=1
        if (int(data2[index][index2])%2==0):
            counter_even_2+=1
        else:
            counter_odd_2+=1

    if(counter_even_1 == counter_even_2 and counter_odd_1 == counter_odd_2):
        counter+=1

print(counter)