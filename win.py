import PySimpleGUI4 as sg
import string 

def make_input_layout(name, key_button, n, prefix="", radio=False):
    layout = [[sg.Text(name)]]

    letters = string.ascii_lowercase[:n]
    for letter in letters:
        layout.append([sg.Input(key=f"-{prefix}{letter}-")])

    layout.append([sg.Button("Valider", key=key_button)])
    return layout
