import os

from zombie_weapons.settings import *

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), ".."))

DEBUG = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'weapons', 'static', 'images')

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates')
)
