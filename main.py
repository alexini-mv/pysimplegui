import PySimpleGUI as sg

layout = [
    [sg.Text("Hola a PySimpleGUI")],
    [sg.Button("OK")]
]

window = sg.Window(
    title="Hola Mundo",
    layout=layout,
    margins=(100,50))

while True:
    event, values = window.read()

    if event == "OK" or event == sg.WIN_CLOSED:
        break

window.close()
