import tkinter as tk
from tkinter import ttk, messagebox
from main_app import abrir_sistema_principal


def tela_login():
    def verificar_login():
        usuario = usuario_entry.get()
        senha = senha_entry.get()
        if usuario == "admin" and senha == "1234":
            login.destroy()
            abrir_sistema_principal()
        else:
            messagebox.showerror("Erro", "Usuário ou senha incorretos")

    login = tk.Tk()
    login.title("Login - Nome do Sistema")
    login.geometry("400x250")
    login.resizable(False, False)

    ttk.Label(login, text="Login", font=("Arial", 20, "bold")).pack(pady=20)

    frame = ttk.Frame(login)
    frame.pack(pady=10)

    ttk.Label(frame, text="Usuário:").grid(row=0, column=0, pady=5, sticky="e")
    usuario_entry = ttk.Entry(frame)
    usuario_entry.grid(row=0, column=1, pady=5)

    ttk.Label(frame, text="Senha:").grid(row=1, column=0, pady=5, sticky="e")
    senha_entry = ttk.Entry(frame, show="*")
    senha_entry.grid(row=1, column=1, pady=5)

    ttk.Button(login, text="Entrar", command=verificar_login).pack(pady=10)

    login.mainloop()
