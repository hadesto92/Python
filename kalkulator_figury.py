from tkinter import *
from tkinter import ttk
import math

def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combined_func


def obwod_trujkata():
    try:
        valueA = float(A.get())
        valueB = float(B.get())
        valueC = float(C.get())
        obwod_t.set(valueA + valueB + valueC)
    except ValueError:
        pass

def pole_trujkata():
    try:
        valueA = float(A.get())
        valueB = float(B.get())
        valueC = float(C.get())
        P = round((valueA + valueB + valueC)/2,2)
        pole_t.set(math.sqrt((P*((P-valueA)*(P-valueB)*(P-valueC)))))
    except ValueError:
        pass

root = Tk()
root.title("Kalkulator")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

A = IntVar()
B = IntVar()
C = IntVar()
pole_t = StringVar()
obwod_t = StringVar()

A_entry = ttk.Entry(mainframe, width=7, textvariable=A)
A_entry.grid(column=3, row=1, sticky=(W, E))

B_entry = ttk.Entry(mainframe, width=7, textvariable=B)
B_entry.grid(column=3, row=2, sticky=(W, E))

C_entry = ttk.Entry(mainframe, width=7, textvariable=C)
C_entry.grid(column=3, row=3, sticky=(W, E))

ttk.Label(mainframe, text="Podaj bok:").grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text="A=").grid(column=2, row=1, sticky=W)
ttk.Label(mainframe, text="jednostek").grid(column=4, row=1, sticky=E)
ttk.Label(mainframe, text="B=").grid(column=2, row=2, sticky=W)
ttk.Label(mainframe, text="jednostek").grid(column=4, row=2, sticky=E)
ttk.Label(mainframe, text="C=").grid(column=2, row=3, sticky=W)
ttk.Label(mainframe, text="jednostek").grid(column=4, row=3, sticky=E)

ttk.Label(mainframe, text="Pole wynosi").grid(column=1, row=4, sticky=E)
ttk.Label(mainframe, textvariable=pole_t).grid(column=3, row=4, sticky=(W, E))
ttk.Label(mainframe, text="j^2").grid(column=4, row=4, sticky=E)
ttk.Label(mainframe, text="Obwód wynosi").grid(column=1, row=5, sticky=E)
ttk.Label(mainframe, textvariable=obwod_t).grid(column=3, row=5, sticky=(W, E))
ttk.Label(mainframe, text="jednostek").grid(column=4, row=5, sticky=E)
ttk.Button(mainframe, text="Policz", command=combine_funcs(pole_trujkata, obwod_trujkata)).grid(column=4, row=6, sticky=E)


for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

A_entry.focus() #sprawdzić co oznacza
B_entry.focus()
C_entry.focus()

root.mainloop()