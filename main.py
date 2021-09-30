# Imports
import PySimpleGUIWeb as sg  # Import PySimpleGUI like this to run as a web app
# import PySimpleGUI as sg  # Import PySimpleGUI like this to run as a desktop app
import logging
import requests
import json

from app_variables import Language_dict
from app_functions import App_Win

# Write Errors To Log File
###############
# Logger
###############

# ------- Configuring Logging File -------- #

# Logger For Log File
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Log File Logging Format
formatter = logging.Formatter("%(asctime)s:%(levelname)s::%(message)s")

# Log File Handler
Log_File_Handler = logging.FileHandler("Translator.log")
Log_File_Handler.setLevel(logging.DEBUG)
Log_File_Handler.setFormatter(formatter)

# Stream Handlers
Stream_Handler = logging.StreamHandler()

# Adding The Handlers
logger.addHandler(Log_File_Handler)
logger.addHandler(Stream_Handler)

logger.debug("")
logger.debug("="*100)

logger.info("Starting App")

# Run App
if __name__ == '__main__':
    
    # Start App
    try:
        APP_WIN = App_Win()

        # Event Loop
        while True:
            app_event, app_values = APP_WIN.read(timeout=10)

            # On Translate
            if (app_event == "TRANSLATE"):
                
                # Check If Source Language Has Been Selected
                if (app_values["-Source_List-"] != "" and app_values["-Source_List-"] != "Select Source Language"):
                    
                    # Check If Target Language Has Been Selected
                    if (app_values["-Target_List-"] != "" and app_values["-Target_List-"] != "Select Target Language"):

                        # Check Source Input Field
                        if(app_values["-Source_Text-"] != "" and app_values["-Source_Text-"] != "Enter Your Text"):
                            Translate = True

                        else:
                            sg.popup("Notification","Enter Text To Transalate",keep_on_top=True)
                            Translate = False
                    
                    else:
                        sg.popup("Notification","Please Select A Target Language",keep_on_top=True)
                        Translate = False

                else:
                    sg.popup("Notification","Please Select A Source Language",keep_on_top=True)
                    Translate = False

                # Get Text
                if Translate == True:
                    Src_Lang = Language_dict[app_values["-Source_List-"]]
                    Trg_Lang = Language_dict[app_values["-Target_List-"]]
                    Input_Text = app_values["-Source_Text-"]

                # # Send Rquest
                URL = f"https://translate.google.com/translate_a/single?client=at&dt=t&dt=ld&dt=qca&dt=rm&dt=bd&dj=1&hl={Trg_Lang}&ie=UTF-8&oe=UTF-8&inputm=2&otf=2&iid=1dd3b944-fa62-4b55-b330-74909a99969e"

                Data = {
                    'sl': Src_Lang,
                    'tl': Trg_Lang,
                    'q': Input_Text
                }

                # Obtain Response
                Response = requests.post(url = URL, data = Data)
                json_data = json.loads(Response.text)

                Translated_Text = ""

                # Display Response
                Translation = json_data["sentences"]
                for i in Translation:
                    try:
                        Translated_Text = f'{Translated_Text}{i["trans"]}'
                    except KeyError:
                        if (i["src_translit"]):
                            pass
                        else:
                            Translated_Text = f'{Translated_Text}**** TRANSLATION MISSING HERE ****\n'
                
                APP_WIN["-Target_Text-"].Update(Translated_Text)
                        

            # Closing App
            if (app_event == sg.WIN_CLOSED):
                APP_WIN.close()
                logger.debug("Closed App")
                break
                            
    except Exception as e:
        logger.exception(e)