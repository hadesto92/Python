#Matura 2017

#Karol Lach

#Podaj jasność najjaśniejszego i jasność najciemnieszego piksela.

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
    number = ''

    for sign in line:
        counter+=1
        if counter <= len(line):
            if sign == ' ':
                tab_pixel.append(int(number))
                number = ''
            else:
                number+=sign
                if(counter == len(line)):
                    tab_pixel.append(int(number))
                    number = ''

#Znalezienie najjaśniejszego i najciemniejszego piksela
max_pixel = 0
min_pixle = 255
for number in tab_pixel:
    if number > max_pixel:
        max_pixel = number
    if number < min_pixle:
        min_pixle = number

print(min_pixle)
print(max_pixel)