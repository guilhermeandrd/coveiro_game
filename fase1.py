import tkinter as tk

fase_1 = tk.Tk();

def iniciar_fase1():

    fase_1.title("Introdução")  
    fase_1.geometry("500x400")
    fase_1.configure(bg="#000000") 
    fase_1.resizable(True, True) 

    title_label = tk.Label(fase_1, 
                        text="O Ladrão de Túmulos", 
                        font=("Vollkorn SC", 28, "bold"), 
                        fg="white", 
                        bg="#000000")
    
    texto_intoduorio = tk.Text(fase_1, height=5, width=50)

    title_label.pack(pady=40)
    texto_intoduorio.insert(tk.END, "Seja Bem vindo Ao Trabalho, Coveiro")
    texto_intoduorio.pack(pady=55)

    fase_1.mainloop()

def inicio():
    return "Seja bem vindo ao trabalho, coveiro"

