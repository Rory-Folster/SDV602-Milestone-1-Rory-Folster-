import PySimpleGUI as sg


def main():
    sg.theme('DefaultNoMoreNagging')

    layout = [
               [sg.Text('Histogram'), sg.Button('Change', key='-HISTOGRAMBTN-'), sg.Text('Pie Chart'), sg.Button('Change', key='-PIECHARTBTN-')],
               [sg.Text(' ')],
               [sg.Multiline(size=(40, 20), key='-GRAPHBOX-')],
               [sg.Text(' ')],
               [sg.Button('Exit', key='-MAINEXITBTN-'), sg.Button('Change keyword', key='-CHANGEKEYWBTN-')]
               ]
    window = sg.Window('Main Application', layout, size=(1000, 700))
    choice = None
    while True:             
        event, values = window.read()
        if event == '-MAINEXITBTN-' or event == sg.WIN_CLOSED:
            break
    window.Close()


def file_selector():

    sg.theme('DefaultNoMoreNagging')

    layout = [
                [sg.Text('Please select a local CSV file.')],
                [sg.Text(' ')],
                [sg.Input(key='FileCSVInput'), sg.FileBrowse(key='-FILEBROWSEBTN-')],
                [sg.Text(' ')],
                [sg.Text('Add any keywords you would like to search for.')],
                [sg.Input(key='-FILEKEYWORDINPUT-')],
                [sg.Text(' ')],
                [sg.Button('Next', key='-FILENEXTBTN-'), sg.Button('Exit', key='-FILEEXITBTN-')]
                ]
    window = sg.Window('Select a file', layout, size=(900, 400), element_justification='c')
    choice = None
    while True:             
        event, values = window.read()
        if event == '-FILEEXITBTN-' or event == sg.WIN_CLOSED:
            break
        if event == "-FILENEXTBTN-":
            main()

    window.Close()



def login():

    sg.theme('DefaultNoMoreNagging')

    layout = [
                [sg.Text('Welcome to my PySimpleGUI application')],
                [sg.Text(' ')],
                [sg.Text('Please enter your username:'), sg.Input(key='-LOGINUSERINPUT-')],
                [sg.Text(' ')],
                [sg.Text('Please enter your password:'), sg.Input(key='-LOGINPASSWORDINPUT-')],
                [sg.Text(' ')],
                [sg.Button('Submit', key="-LOGINSUBMITBTN-")],
                [sg.Text(' ')],
                [sg.Button('Exit application', key="-LOGINEXITBTN-")]
                ]
    window = sg.Window("Main Application", layout, size=(900, 400), element_justification='c')
    while True:             
        event, values = window.read()
        if event == '-LOGINEXITBTN-' or event == sg.WIN_CLOSED:
            break
        if event == "-LOGINSUBMITBTN-":
            file_selector()


    window.Close()

if __name__ == "__main__":
    login()