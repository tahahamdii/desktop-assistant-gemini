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