import sys
import time
import random
import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/andbv/Downloads/Proyecto102/Archivos_Documentos"

class FileEventHandler(FileSystemEventHandler):

    def on_created(self, event):
        print(f"!Oye {event.src_path} ha sido creado")

    def on_modified(self, event):
        print(f"!lo siento! !Alguien borro {event.src_path}!")

    def on_moved(self, event):
        print(f"Se ha movido/renombrado {event.src_path} a {event.dest_path}")

    def on_deleted(self, event):
        print(f"!Oye se ha eliminado {event.src_path}")
