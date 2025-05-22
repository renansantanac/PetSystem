import tkinter as tk
from tkinter import ttk
from cadastro import CadastroApp
from agendamento import AgendamentoApp
from financeiro import FinanceiroApp
from fichas import FichasApp


def abrir_sistema_principal():
    app = tk.Tk()
    app.title("Sistema Petshop - Distrito Pet")
    app.geometry("1000x600")
    app.resizable(True, True)

    ttk.Label(app, text="Distrito Pet - Sistema de Gestão", font=("Arial", 20, "bold")).pack(pady=15)

    menu = ttk.Frame(app)
    menu.pack(pady=20)

    ttk.Button(menu, text="Cadastro de Clientes/Pets", width=30, command=lambda: CadastroApp(tk.Toplevel(app))).grid(row=0, column=0, padx=10, pady=10)
    ttk.Button(menu, text="Agendamento de Serviços", width=30, command=lambda: AgendamentoApp(tk.Toplevel(app))).grid(row=0, column=1, padx=10, pady=10)
    ttk.Button(menu, text="Fichas dos Clientes", width=30, command=lambda: FichasApp(tk.Toplevel(app))).grid(row=1, column=0, padx=10, pady=10)
    ttk.Button(menu, text="Controle Financeiro", width=30, command=lambda: FinanceiroApp(tk.Toplevel(app))).grid(row=1, column=1, padx=10, pady=10)
    ttk.Button(menu, text="Sair", width=20, command=app.destroy).grid(row=2, column=0, columnspan=2, pady=20)

    app.mainloop()
