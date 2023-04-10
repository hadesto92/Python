#Matura 2017

#Karol Lach

#Podaj długość najdłuższej lini pionowej (czyli ciągu kolejnych pikseli w tej samej kolumnie obrazka), złożonej z pikseli
# tej samej jasności.

#Wczytanie pliku do zmiennej
file_temp = open("dane.txt", "r")
content = file_temp.read()
content_temp = content.split("\n")

#Zliczenie wierszy
content_len = len(content_temp)

#Zapisanie pikseli do listy
tab_pixel = []
for line in content_temp:
    counter=0
    if line == '':
        break
    numbers = []
    sign_number = ''

    for sign in line:
        counter+=1
        if counter <= len(line):
            if sign == ' ':
                numbers.append(int(sign_number))
                sign_number = ''
            else:
                sign_number+=sign
                if(counter==len(line)):
                    numbers.append(int(sign_number))
                    sign_number = ''

    tab_pixel.append(numbers)

#Sprawdzenie w każdej kolumnie każdą linijkę pokoleji czy piksele są sobie równe i zapisanie wyniku
result=[]
for kol in range(320):
    temp=1
    for line in range(199):
        if tab_pixel[line][kol] == tab_pixel[line+1][kol]:
            temp+=1
        else:
            result.append(temp)
            temp=1

print(max(result))
