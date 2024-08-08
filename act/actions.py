import os
import subprocess as sp
from audio.speech import speak
from PIL import ImageGrab
from decouple import config
from act.screenrecord import record_screen, stop_recording
import threading
from aim.vision import describe_image
import webbrowser
from audio.speech import speak, listen


def open_cmd():
    os.system('start cmd')

def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)

def open_website():
    speak('Which website would you like to open?')
    url = listen().lower()
    webbrowser.open(url)

def take_screenshot():
    media_dir=config("MEDIA_DIR")
    screenshot_file=config("SCREENSHOT_FILE")
    screenshot = ImageGrab.grab()
    screenshot.save(media_dir + "/" + screenshot_file)
    print("Screenshot saved as: " +  screenshot_file)
    speak("Screenshot saved as " + screenshot_file)
