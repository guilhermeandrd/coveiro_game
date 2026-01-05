import pygame

import tkinter as tk
from tkinter import messagebox
from tkinter import font


pygame.mixer.init()
pygame.mixer.music.load("arquivos_mp3/erro_pessoaviva.mp3")
pygame.mixer.music.play()





root = tk.Tk()

font_families = font.families()

root.title("") 
root.geometry("500x400")  
root.configure(bg="#000000")
root.resizable(False, False)


title_label = tk.Label(root, 
                       text="Coveiro Game", 
                       font=("Vollkorn SC", 28, "bold"), 
                       fg="white", 
                       bg="#000000")

texto_intoduorio = tk.Text(root, height=5, width=50)

title_label.pack(pady=40)
texto_intoduorio.insert(tk.END, "Como você pôde?\n")
texto_intoduorio.insert(tk.END, "Tanta vida restante \n")
texto_intoduorio.insert(tk.END, "Como você ousa?  \n")
texto_intoduorio.insert(tk.END, "Você crava a pá na cabeça dele\n")
texto_intoduorio.insert(tk.END, "Morto\n")
texto_intoduorio.insert(tk.END, "Morto...\n")
texto_intoduorio.pack(pady=55)

title_label.pack(pady=40)

root.mainloop()