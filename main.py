import win, fx, random as rdm
import PySimpleGUI4 as sg
import matplotlib.pyplot as plt

affine_layout = win.make_input_layout("Entrer f(x) = ax+b", "v", 2, prefix="a")
quadra_layout = win.make_input_layout("Entrer f(x) = ax² + bx + c", "v2", 3, prefix="q")


window = sg.Window("fonction", affine_layout + quadra_layout, size =(400,400))

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == "Quitter":
        break

    if event == "v" :

        # A
        if values["-aa-"] == "":
            a_val = rdm.randint(-5,5)
        else:
            try:
                a_val = int(values["-aa-"])
            except ValueError:
                sg.popup_error("Entrez un nombre entier !")
                continue 
        # B
        if values["-ab-"] == "":
            b_val = rdm.randint(-5,5)
        else:
            try:
                b_val = int(values["-ab-"])
            except ValueError:
                sg.popup_error("Entrez un nombre entier !")
                continue

        affine = fx.Mkaffine(a=a_val, b=b_val)
        affine.show()



    if event == "v2" :
        # A
        if values["-qa-"] == "":
            a_val = rdm.randint(-5,5)
        else:
            try:
                a_val = int(values["-qa-"])
            except ValueError:
                sg.popup_error("Entrez un nombre entier !")
                continue 
        # B
        if values["-qb-"] == "":
            b_val = rdm.randint(-5,5)
        else:
            try:
                b_val = int(values["-qb-"])
            except ValueError:
                sg.popup_error("Entrez un nombre entier !")
                continue
        # C
        if values["-qc-"] == "":
            c_val = rdm.randint(-5,5)
        else:
            try:
                c_val = int(values["-qc-"])
            except ValueError:
                sg.popup_error("Entrez un nombre entier !")
                continue

        quadra = fx.Mkquadra(a=a_val, b=b_val, c=c_val)
        quadra.show()
        
