import tkinter as tk 


def mostrar():
    mostrar_nome=entry_nome.get()
    mostrar_text.config(text=mostrar_nome)

janela=tk.Tk()

janela.geometry('500x500')
nome=tk.Label(janela,text='Nome')
nome.pack(pady=10)


entry_nome=tk.Entry(janela)
entry_nome.pack(pady=10)

mostrar_text=tk.Label(janela,text='')
mostrar_text.pack(pady=10)

btn=tk.Button(janela,text="Registrar o nome",command=mostrar)
btn.pack(pady=10)

janela.mainloop()
