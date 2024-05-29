#!/usr/bin/env python
import sys
import PySimpleGUI as sg
import subprocess
import os
import webbrowser

"""
    Demo_Toolbar - A floating toolbar with quick launcher
    
    One cool PySimpleGUI demo. Shows borderless windows, grab_anywhere, tight button layout
    You can setup a specific program to launch when a button is clicked, or use the
    Combobox to select a .py file found in the root folder, and run that file.
    
"""

ROOT_PATH = './'



def Launcher():

    sg.theme('LightBlue6')

    namesonly = [f for f in os.listdir(ROOT_PATH) if f.endswith('.py')]

    if len(namesonly) == 0:
        namesonly = ['test 1', 'test 2', 'test 3']

    sg.set_options(element_padding=(0, 0),
        button_element_size=(17, 3), auto_size_buttons=False, font=('Arial',12,'bold'),auto_size_text=False)

    layout = [[#sg.Combo(values=namesonly, size=(35, 30), key='demofile'),
               sg.Button('Sharepoint PCP', button_color=('white','#0070C0')),
               sg.Button('Métricas Manufatura', button_color=('White', '#2F5597')),
               sg.Button('Métricas Montagem', button_color=('White', '#2F5597')),
               sg.Button('Métricas MPS', button_color=('White', '#2F5597')),
               sg.Button('Andon', button_color=('White', '#66A2D8')),
               sg.Button('Lead Time', button_color=('White', '#66A2D8')),
               #sg.Button('Fila de roteiros',button_color=('White', '#66A2D8')),
              [sg.Text('', text_color='white', size=(17, 1), key='output',auto_size_text=True,)]]]
            

    window = sg.Window('Floating Toolbar',
                       layout,
                       no_titlebar=True,
                       grab_anywhere=True,
                       keep_on_top=True,
                       resizable=False,
                       
                       )


    # ---===--- Loop taking in user input and executing appropriate program --- #
    while True:
        event, values = window.read()
        if event == 'Exit' or event == sg.WIN_CLOSED:
            break           # exit button clicked
        if event == 'Sharepoint PCP':
            webbrowser.open("https://digicorner.sharepoint.com/sites/PCPSharepoint") 
        elif event == 'Métricas Manufatura':
            webbrowser.open("https://app.powerbi.com/groups/a9ef9509-560f-4732-be82-94635985717b/reports/53611b6a-3264-43e3-874f-7d8b7629a1fa/ReportSection")
        elif event == 'Métricas Montagem':
            webbrowser.open("https://app.powerbi.com/groups/e03598b8-9927-405a-97d1-24731bebbbbb/reports/1bb594c1-a35b-482f-96c8-cb86e1ef72a8/ReportSection")    
        elif event == 'Métricas MPS':
            webbrowser.open("https://app.powerbi.com/groups/me/reports/2147c246-bb88-4076-94a5-a3260465ca5c/ReportSection")
        elif event == 'Andon':
            webbrowser.open("http://bra01vivs0130.digicorner.intra/maptronix/andon_graf.html")
        #elif event == 'Fila de Roteiro':
          #  webbrowser.open("https://digicorner.sharepoint.com/:x:/r/sites/EngIndUsinagem/_layouts/15/Doc.aspx?sourcedoc=%7B0A3A0701-BC44-4920-880B-A1FB52762A45%7D&file=Obeya%20Manufacturing%20Package.xlsx&action=default&mobileredirect=true&cid=a309c879-4b1c-4930-b221-00e0735ec9e0")     
        elif event == 'Lead Time':
            webbrowser.open("https://digicorner.sharepoint.com/sites/PlanejamentodeProducao/Shared%20Documents/Forms/AllItems.aspx?FolderCTID=0x0120002B54383267179949AE1846DE52A92456&id=%2Fsites%2FPlanejamentodeProducao%2FShared%20Documents%2FIndicadores%2FManufatura&viewid=435b4dbd%2D3349%2D4309%2Db9aa%2D6c792356a250")     

            #file = values['demofile']
            #print('Launching %s' % file)
            #ExecuteCommandSubprocess('python', os.path.join(ROOT_PATH, file))
        else:
            print(event)
            
    window.close()


def ExecuteCommandSubprocess(command, *args, wait=False):
    try:
        if sys.platform == 'linux':
            arg_string = ''
            arg_string = ' '.join([str(arg) for arg in args])
           #  for arg in args:
            #     arg_string += ' ' + str(arg)
            print('python3 ' + arg_string)
            sp = subprocess.Popen(['python3 ', arg_string],
                                  shell=True,
                                  stdout=subprocess.PIPE,
                                  stderr=subprocess.PIPE)
        else:
            arg_string = ' '.join([str(arg) for arg in args])
            sp = subprocess.Popen([command, arg_string],
                                  shell=True,
                                  stdout=subprocess.PIPE,
                                  stderr=subprocess.PIPE)
            # sp = subprocess.Popen([command, list(args)], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        if wait:
            out, err = sp.communicate()
            if out:
                print(out.decode("utf-8"))
            if err:
                print(err.decode("utf-8"))
    except:
        pass


if __name__ == '__main__':
    Launcher()
