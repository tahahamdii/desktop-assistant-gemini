from audio.speech import speak, listen
from decouple import config
from aim.conv import converse
from act.actions import open_notepad, open_word, open_excel, open_ppt, open_calculator, open_cmd, take_screenshot, start_screen_record, stop_screen_record, open_camera, camera_vision, open_website
import threading
import ui.gui as gui
import time

BOT_NAME = config("VA_NAME")

exit_event = threading.Event()

if __name__ == '__main__':
    awake = True


    speak(f"I am your {BOT_NAME}. How may I help you?")

    while True:
        query = listen()
        if query == None:
            continue
        else:
            query = query.lower()
            intent = converse(query)

        print(query)
        print(intent)

        if not intent.startswith('ACTION_'):
            speak(intent)

        if intent == 'ACTION_AWAKEN':
            awake = True
            speak("How can I help you Sir?")
            continue

        elif intent == 'ACTION_SLEEP':
            awake = False
            speak("Hibernating now")
            continue

        if not awake:
            print("Currently hibernating...Zzzz...nothing to do.")
            continue

        elif intent == 'ACTION_EXIT':
            speak('Have a good day Sir')
            time.sleep(4)
            exit(1)



        elif intent == 'ACTION_MINIMIZE_DISAPPEAR_APPLICATION':
            gui.disappear()





        elif intent == 'ACTION_OPEN_COMMAND_PROMPT':
            open_cmd()

        elif intent == 'ACTION_OPEN_CALCULATOR':
            open_calculator()

        elif intent == "ACTION_OPEN_BROWSER_WEBSITE":
            open_website()

        elif intent == "ACTION_TAKE_SCREENSHOT":
            take_screenshot()

        elif intent == "ACTION_START_SCREEN_RECORDING":
            start_screen_record()

        elif intent == "ACTION_STOP_SCREEN_RECORDING":
            stop_screen_record()

        elif intent == "ACTION_OPEN_CAMERA":
            open_camera()

        elif intent == "ACTION_WHAT_DO_YOU_SEE_IN_CAMERA":
            camera_vision()

