import tkinter as tk
import pygame
import os

root = tk.Tk()
root.title('amp3_player')
root.geometry("500x300")

pygame.mixer.init()

songlist = tk.Listbox(root, bg="black", fg="white", width=100, height=15)
songlist.pack()

root.mainloop()