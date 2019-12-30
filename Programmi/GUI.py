import PySimpleGUI as sg      




sg.Popup('Hello From PySimpleGUI!', 'This is the shortest GUI program ever!')
event, (filename,) = sg.Window('Get filename example'). Layout([[sg.Text('Filename')], [sg.Input(), sg.FileBrowse()], [sg.OK(), sg.Cancel()] ]).Read()
print (filename)
