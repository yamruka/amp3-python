import tkinter as tk
import pygame
import sys
import os

root = tk.Tk()
root.title('amp3_player')
root.geometry("500x300")
songlist = tk.Listbox(root, bg="black", fg="white", width=100, height=15)
songlist.pack()

def on_close():
    pygame.mixer.quit()
    root.destroy() 
    root.destroy()
    sys.exit()
    os._exit()


root.protocol("WM_DELETE_WINDOW", on_close)
root.mainloop()

pygame.mixer.init()

