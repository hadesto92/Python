#Matura 2017

#Karol Lach

#Sąsiednie piksele to takie, które leżą obok siebie w tym samym wierszu lub w tej samej kolumnie. Dwa sąsiednie piksele
# nazywamy kontrastującymi, jeśli ich wartości różnią się o więcej niż 128. Podaj liczbę wszystkich takich pikseli, dla
# których istnieje przynajmniej jeden kontrastujący z nim sąsiedni piksel.

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

#Zliczanie kontrastujących pikseli
result = 0
counter_line = 0
for line in tab_pixel:
    counter_sign = 0
    for sign in line:
        if counter_line>0 and abs(tab_pixel[counter_line-1][counter_sign]-tab_pixel[counter_line][counter_sign])>128:
            result+=1
        elif counter_line<199 and abs(tab_pixel[counter_line+1][counter_sign]-tab_pixel[counter_line][counter_sign])>128:
            result+=1
        elif counter_sign>0 and abs(tab_pixel[counter_line][counter_sign-1]-tab_pixel[counter_line][counter_sign])>128:
            result+=1
        elif counter_sign<319 and abs(tab_pixel[counter_line][counter_sign+1]-tab_pixel[counter_line][counter_sign])>128:
            result+=1
        counter_sign+=1
    counter_line+=1

print(result)
