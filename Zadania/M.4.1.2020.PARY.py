#Matura 2020

#Karol Lach

#Mocna hipoteza Goldbacha mówi, że każda parzysta liczba całkowita większa od 4 jest sumą dwóch nieparzystych liczb pierwszych,
# np. liczba 20 jest równa sumie 3+17 lub sumie 7+13. Każdą liczbę parzystą z pliku pary.txt przedstaw w postaci sumy dwóch liczb
# pierwszych. Wypisz tę liczbę oraz dwa składniki sumy w kolejności niemalejącej. Jeśli istnieje więcej rowzwiązań
# (tak jak w przypadku liczby 20) należy wypisać składniki sumy o największej różnicy. Wyniki podaj w oddzielnych wierszach,
# w kolejności zgodnej z kolejnością danych w pliku pary.txt. Liczby w każdym wierszu rozdziel znakiem spacji, np. dla liczby 20
# należy wypisać 20 3 17.

#Wczytanie pliku do zmiennej
file_temp = open("pary.txt", "r")
content = file_temp.read()
content_temp = content.split("\n")

#Zapisanie wczytanego pliku do listy
tab_pair = []
for line in content_temp:
    tab_temp = []
    temp_sing=''
    for sign in line:
        if sign!=' ':
            temp_sing+=sign
        else:
            tab_temp.append(temp_sing)
            temp_sing = ''
    tab_temp.append(temp_sing)
    tab_pair.append(tab_temp)

#print(tab_pair)

#Funkcja sprawdzająca czy podana liczba jest liczbą pierwszą
def number_firstly(number):
    if number == 2:
        return True
    if number % 2 == 0 or number <= 1:
        return False

    for int in range(3, number, 2): #Zaczyam pętlę od liczby 3 idę do liczby number przeskakująć o dwie liczby w każdje z pętli
        if(number%int == 0):
            return False

    return True

#Sprwadzenie która liczba jest parzysta i większa od 4
for index in range(len(tab_pair)-1):
    if(int(tab_pair[index][0])%2==0 and int(tab_pair[index][0])>4):
        #Utworzenie pętli i sprawdzenie pierwszej liczby nieparzystej czy jest liczbą pierwszą
        for number_index in range(int(tab_pair[index][0])):
            #Sprawdzenie czy różnica liczby parzystej i pierwszej nieparzystej jest liczbą pierwszą jeśli nie szuka kolejnej liczby pierwszej która będzie liczbą pierwszą
            if(number_firstly(number_index) and number_firstly(int(tab_pair[index][0])-number_index)):
                print(int(tab_pair[index][0]), number_index, int(tab_pair[index][0])-number_index)
                break

