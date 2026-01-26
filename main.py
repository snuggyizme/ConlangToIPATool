from config import tools as configTools
from config import make as makeConfig

import FreeSimpleGUI as fsGUI
fsGUI.theme("LightGrey1")

homeLayout = [[fsGUI.Text("IPAt")],
              [fsGUI.Button("Import/Create a language config"), fsGUI.Button("Create IPA for words"), fsGUI.Button("Close")]]

importOrCreateLayout = [
    [fsGUI.Button("Import (Paste from clipboard)")],
    [fsGUI.Button("Import (Select File)")],
    [fsGUI.Button("Make new")],
    [fsGUI.Button("Back")]
]

def main():
    window = fsGUI.Window("IPAt", homeLayout, no_titlebar=True, grab_anywhere=True)

    while True:
        event, values = window.read()
        if event == "Close":
            break

        if event == "Import/Create a language config":
            IoCwindow = fsGUI.Window("IPAt", importOrCreateLayout, no_titlebar=True, grab_anywhere=True)

            while True:
                IoCevent, IoCvalues = IoCwindow.read()
                if event == "Close":
                    break

                if event == "Import (Paste from clipboard)":
                    pass

                if event == "Import (Select File)":
                    pass
                
                if event == "Make new":
                    pass

                if event == "Back":
                    break


def testLine():
    print(configTools.compileDefault(configTools.default))
    print(configTools.extractLanguage(configTools.defaultCompiled))

if __name__ == "__main__":
    main()
