import pygame
from fase1 import fase_1, iniciar_fase1

import tkinter as tk
from tkinter import messagebox
from tkinter import font



fase_1.destroy()

pygame.mixer.init()
pygame.mixer.music.load("arquivos_mp3/marchafunebre")

pygame.mixer.music.play()

def iniciar_jogo():
    """
    Esta função será chamada quando o botão 'Iniciar Jogo' for clicado.
    """
    print("Iniciando o jogo... (Aqui você chamaria seu loop de jogo)")
    
    root.destroy() 
    
    pygame.mixer.music.stop()
    fase_1.__init__()
    iniciar_fase1()

    

def abrir_opcoes():
    """
    Função para o botão 'Opções'. 
    Por enquanto, ela só abre uma caixa de diálogo.
    """
    messagebox.showinfo("Opções", 
                        "Configurações do Jogo:\n\n- Som: Ligado\n- Dificuldade: Normal")

def sair_do_jogo():
    """
    Função para fechar o aplicativo.
    """
    print("Fechando o jogo...")
    root.quit() 



root = tk.Tk()

font_families = font.families()

root.title("Coveiro Game - Menu Principal") 
root.geometry("500x400")  
root.configure(bg="#000000")
root.resizable(False, False)


title_label = tk.Label(root, 
                       text="Coveiro Game", 
                       font=("Vollkorn SC", 28, "bold"), 
                       fg="white", 
                       bg="#000000")


start_button = tk.Button(root, 
                         text="Iniciar Jogo", 
                         font=("Vollkorn SC", 16),
                         bg="#424242", 
                         fg="white",
                         width=20,   
                         command=iniciar_jogo)


options_button = tk.Button(root, 
                           text="Opções", 
                           font=("Vollkorn SC", 16),
                           bg="#252323",  
                           fg="white",
                           width=20,
                           command=abrir_opcoes)


exit_button = tk.Button(root, 
                        text="Sair", 
                        font=("Vollkorn SC", 16),
                        bg="#1A1919", 
                        fg="white",
                        width=20,
                        command=sair_do_jogo)




title_label.pack(pady=40)
start_button.pack(pady=15)
options_button.pack(pady=15)
exit_button.pack(pady=15)



root.mainloop()