#Matura 2019

#Karol Lach

#W pliku liczby3.txt znajdź najdłuższy ciąg liczb występujących kolejno po sobie i taki, że największy współny dzielnik ich
# wszystkich jest większy od 1 (innym słowy: istnieje taka liczba całkowita większa od 1, która jest dzielnikiem każdej
# z tych liczb). Jako odpowiedź podaj wartość pierwszej liczby w takim ciągu, długość ciągu oraz największą liczbę całkowitą,
# która jest dzielnikiem każdej liczy w tym ciągu. W pliku z danymi jest tylko ejeden taki ciąg o największej długości.

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

#Stworzenie funkcji NWD korzystająć z algorytmu Euklidesa
def NWD(a, b):
    if a%b == 0:
        return b
    else:
        return NWD(b,a%b)

#print(NWD(40,90))

#Przejście przez listę i sprawdzenie za pomocą NWD każdej liczby
counter = 0
first_number_in_series = 0
max_NWD = 0
len_series = 0
for number in number_list:
    if counter < len(number_list)-2:
        len_series_temp = 1
        max_NWD_temp = NWD(int(number), int(number_list[counter+len_series_temp]))
        while max_NWD_temp > 1 and len_series_temp<len(number_list)-counter:
            if len_series_temp > len_series:
                first_number_in_series = number
                len_series = len_series_temp
                max_NWD = max_NWD_temp
            max_NWD_temp = NWD(max_NWD_temp, int(number_list[counter+len_series_temp]))
            len_series_temp += 1
    counter+=1

print(first_number_in_series, len_series, max_NWD)

