#Matura 2017

#Karol Lach

#Podaj, ile wynosi najmniejsza liczba wierszy, które należy usunąć, żeby obraz miał pionową oś symetri. Obraz ma pionową
# oś symetri, jeśli w każdym wierszu i-ty piksel od lewej strony przyjmuje tę samą wartość, co i-ty piksel od prawej strony,
# dla dowolnego 1<=i<=320.

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


#Sprawdzenie każdej lini czy piksele są sobie równe jeśli nie zwiększamy licznik lini do usunięcia
counter = 0
for line in tab_pixel:
    if line != line[::-1]:
        counter+=1

print(counter)
