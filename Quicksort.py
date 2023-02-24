def partition(tab,low,high):
    i = (low-1) #indeks najniższego elementu w tabeli od 0
    temp = tab[high] #ostatni elemnt w tabeli

    for j in range(low,high):
        if tab[j]<=temp: #zamiana miejscami dopuki niezostanie osiągnięty ostatni element
            i+=1
            tab[i],tab[j]=tab[j],tab[i] #zamiana
            """
            temp2 = tab[i]
            tab[i] = tab[j]
            tab[j] = temp2
            """
    tab[i+1],tab[high]=tab[high],tab[i+1]
    return(i+1)

def qSort(tab,low,high):
    if low < high:
        pi = partition(tab,low,high)

        qSort(tab,low,pi-1)
        qSort(tab,pi+1,high)


def quickSort(tab):
    qSort(tab,0,(len(tab)-1))
    return tab
