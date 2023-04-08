#Matura 2019

#Karol Lach

#Podaj, w kolejnośći ich wysępowania w pliku liczby3.txt, wszystkie liczby, które są równe sumie silni swoich cyfr.

#Wczytanie pliku do zmiennej
file_temp = open("liczby3.txt", "r")
content = file_temp.read()
content_temp = content.split("\n")

#Zliczenie wierszy
content_len = len(content.split("\n"))

#Zapisanie liczb do listy
number_list = []

for line in content_temp:
    if line == '':
        break
    number_list.append(line)

#Stworzenie funkcji silni
def silnia(arg):
    if arg == 0:
        return 1
    else:
        return arg*silnia(arg-1)

#print(silnia(5))

#Sprawdzenie czy każda z cyfr tworzących liczbę po smumowaniu daje wynik liczby
for number in number_list:
    sum = 0
    for sign in number:
        sum+=silnia(int(sign))
    #print(sum)

    if sum == int(number):
        print(number)