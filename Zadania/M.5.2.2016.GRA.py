#Matura 2020

#Karol Lach

#Podaj liczbę żywych komórek w drugim pokoleniu tego układu.

#Wczytanie pliku do zmiennej
file_temp = open("gra.txt", "r")
content = file_temp.read()
content_temp = content.split("\n")

#Utworzenie listy która będzie trzymała pokolenia pierwszy wymiar numer pololenia drugi wymiar poszczególne linijki pokolenia.
tab_game = []
temp_tab = []
for line in content_temp:
    temp_tab.append(line)
tab_game.append(temp_tab)

#print(tab_game)

#Funkcja sprawdzająca czy podany argument ma swoich sąsiadów żywych jeśli tak zwraca liczbę ile ich jest
def neighbours(tab_generation=[], number_generation=0, row=0, col=0):

    results = 0

    for i_row in range(-1, 2):
        for i_col in range(-1, 2):
            if not(i_row == i_col == 0):
                if(tab_generation[number_generation][(row+i_row)%len(tab_generation[number_generation])][(col+i_col)%len(tab_generation[number_generation][row])] == 'X'):
                    results+=1

    return results

#print(neighbours(tab_game,0,4,8))

#Stworzenie funkcji która będzie tworzyć kolejne pokolenia
def generation(tab_generation=[], number_generation=1):
    for index in range(number_generation-1):
        tab_line_temp = []
        for i in range(len(tab_generation[index])):
            line = ''
            for j in range(len(tab_generation[index][i])):

                if(tab_generation[index][i][j]=='X' and (neighbours(tab_generation,index,i,j)==2 or neighbours(tab_generation,index,i,j)==3)):
                    line+='X'
                elif(tab_generation[index][i][j]=='.' and neighbours(tab_generation,index,i,j)==3):
                    line+='X'
                else:
                    line+='.'
            tab_line_temp.append(line)
        tab_generation.append(tab_line_temp)

    return tab_generation

#Stworzenie funkcji sprawdzającej ile komórek żyje w danym pokoleniu
def life_generation(tab_generation=[], number_generation=0):

    result = 0

    for i in range(len(tab_generation[number_generation])):
        for j in range(len(tab_generation[number_generation][i])):
            if(tab_generation[number_generation][i][j]=='X'):
                result+=1

    return result

print(life_generation(generation(tab_game,2),1))