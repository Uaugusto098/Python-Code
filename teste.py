import tkinter as tk
import webbrowser

# Dicionários de URLs
classtm = {
    "pp": "https://www.wallsgeneralstore.com.br/class?loja=690339&categoria=119&variants%5B%5D=Tamanho%7C%7CPP",
    "p": "https://www.wallsgeneralstore.com.br/class?loja=690339&categoria=119&variants%5B%5D=Tamanho%7C%7CP",
    "m": "https://www.wallsgeneralstore.com.br/class?loja=690339&categoria=119&variants%5B%5D=Tamanho%7C%7CM",
    "g": "https://www.wallsgeneralstore.com.br/class?loja=690339&categoria=119&variants%5B%5D=Tamanho%7C%7CG",
    "gg": "https://www.wallsgeneralstore.com.br/class?loja=690339&categoria=119&variants%5B%5D=Tamanho%7C%7CGG",
    "egg": "https://www.wallsgeneralstore.com.br/class?loja=690339&categoria=119&variants%5B%5D=Tamanho%7C%7CEGG"
}

suftm = {
    "pp": "https://streetbusiness.com.br/marca/sufgang/?Tamanho=Pp",
    "p": "https://streetbusiness.com.br/marca/sufgang/?Tamanho=P",
    "m": "https://streetbusiness.com.br/marca/sufgang/?Tamanho=M",
    "g": "https://streetbusiness.com.br/marca/sufgang/?Tamanho=G",
    "gg": "https://streetbusiness.com.br/marca/sufgang/?Tamanho=Gg",
    "exg": "https://streetbusiness.com.br/marca/sufgang/?Tamanho=Exg",
    "exgg": "https://streetbusiness.com.br/marca/sufgang/?Tamanho=Exgg"
}

madtm = {
    "pp": "https://streetbusiness.com.br/marca/mad-enlatados/?Tamanho=Pp",
    "p": "https://streetbusiness.com.br/marca/mad-enlatados/?Tamanho=P",
    "m": "https://streetbusiness.com.br/marca/mad-enlatados/?Tamanho=M",
    "g": "https://streetbusiness.com.br/marca/mad-enlatados/?Tamanho=G",
    "gg": "https://streetbusiness.com.br/marca/mad-enlatados/?Tamanho=Gg",
    "exg": "https://streetbusiness.com.br/marca/mad-enlatados/?Tamanho=Exg",
    "exgg": "https://streetbusiness.com.br/marca/mad-enlatados/?Tamanho=Exgg"
}

# Função para abrir link com base na seleção
def abrir_link():
    marca = marca_var.get()
    tamanho = tamanho_var.get()

    if marca == "Sufgang":
        url = suftm.get(tamanho, "")
    elif marca == "Class":
        url = classtm.get(tamanho, "")
    elif marca == "Mad":
        url = madtm.get(tamanho, "")
    else:
        url = ""

    if url:
        webbrowser.open(url)

# Criando a janela principal
root = tk.Tk()
root.title("Consulta de Roupas")

# Dropdown para selecionar a marca
tk.Label(root, text="Selecione a marca:", font=("Arial", 12)).pack(pady=5)
marca_var = tk.StringVar()
marca_var.set("Sufgang")  # Valor padrão
marca_menu = tk.OptionMenu(root, marca_var, "Sufgang", "Class", "Mad")
marca_menu.pack()

# Dropdown para selecionar o tamanho
tk.Label(root, text="Selecione o tamanho:", font=("Arial", 12)).pack(pady=5)
tamanho_var = tk.StringVar()
tamanho_var.set("pp")  # Valor padrão
tamanho_menu = tk.OptionMenu(root, tamanho_var, *classtm.keys())
tamanho_menu.pack()

# Botão para consultar
tk.Button(root, text="Consultar", command=abrir_link, font=("Arial", 12)).pack(pady=10)

# Iniciando a interface gráfica
root.mainloop()
