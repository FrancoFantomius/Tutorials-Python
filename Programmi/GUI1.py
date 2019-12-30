import PySimpleGUI as sg

layout = [
    [sg.Text('Login')],
    [sg.Text('Email', size=(15, 1)), sg.InputText()],
    [sg.Text('Password', size=(15, 1)), sg.InputText(password_char='*')],
    [sg.Submit(), sg.Cancel()]
]

window = sg.Window('Esempio di login').Layout(layout)
button, values = window.Read()

print(button, values[0], values[1])
