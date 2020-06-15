from pathlib import Path
from time import sleep
from watchdog.observers import Observer
from EventHandler import EventHandler
import tkinter as tk
import os
from tkinter import filedialog, Text


root = tk.Tk()
canvas = tk.Canvas(root, height=700, width = 700, bg="#FFFFFF")
root.mainloop();



if __name__ == '__main__':
    watch_path = Path.home() / 'Downloads'
    print(watch_path)
    destination_root = Path.home() / 'Desktop/FileforFiles'
    print(destination_root)
    event_handler = EventHandler(watch_path=watch_path, destination_root=destination_root)

    observer = Observer()
    observer.schedule(event_handler, f'{watch_path}', recursive=True)
    observer.start()

    try:
        while True:
            sleep(60)
            print('running')
    except KeyboardInterrupt:
        observer.stop()
        print('stopped')
    observer.join()