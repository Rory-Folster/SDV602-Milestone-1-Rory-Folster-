import PySimpleGUI as sg;


def demo1():
    layout = [
        [
            sg.Text("This is row 1")
        ], [
            sg.Text('Username:', size=(15, 1)),
            sg.InputText(key="source"),
            sg.FolderBrowse(target="source")
        ], [
            sg.Text('Destination folder', size=(15, 1)),
            sg.InputText(key="destination"),
            sg.FolderBrowse(target="destination")
        ], [
            sg.Checkbox("Delete files in destination that don't exist in source", default=False, key="delete_nonexisting")
        ], [
            sg.Submit(), sg.Cancel()
        ]
    ]
    window = sg.Window('Folder synchronisation').Layout(layout)
    while True:
        event, values = window.Read()
        if event == "Submit":
            return values
        elif event is None or event == "Cancel":
            return None

if __name__ == "__main__":
    result = demo1()
    print(result)
