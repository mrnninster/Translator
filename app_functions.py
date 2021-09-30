import PySimpleGUI as sg
from app_variables import Language_dict

# Applicaion Window Function
def App_Win():

    # Window Location And Size
    Display_Width = 350
    Display_Height = 650
    Initial_X = 400
    Initial_Y  = 50

    # Source Language Section
    From_List = [sg.Combo([x for x in Language_dict.keys()], default_value="Select Source Language", key=("-Source_List-"), size=(45,1))]
    From_Text = [sg.Multiline(default_text = 'Enter Your Text', size=(45,15), key=("-Source_Text-"))]

    # Destination Language Section
    Target_List = [sg.Combo([x for x in Language_dict.keys()], default_value="Select Target Language", key=("-Target_List-"), size=(45,1))]
    Target_Text = [sg.Multiline(default_text="Translation Will Appear Here", size=(45,15), key=("-Target_Text-"),disabled=True)]

    # Seperator 
    H_Seperator = [[sg.Text("-"*80)]]

    # Translate Button
    Translate_Button = [sg.Button("TRANSLATE", button_color=("white","green"), enable_events=True, font=("Courier 15",15), size=(45,1))]

    # Left Section
    Left_Section = [
        From_List,From_Text
    ]

    # Right Sction
    Right_Section = [
        Target_List,Target_Text,
    ]

    # App Window Layout
    Window_Layout = [[Left_Section,H_Seperator,Right_Section,Translate_Button]]

    # Create Window
    TA_Win = sg.Window('Translator App', Window_Layout, location=(Initial_X, Initial_Y), size=(Display_Width,Display_Height), keep_on_top=True, finalize=True)
    return TA_Win