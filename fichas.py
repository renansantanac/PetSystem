import tkinter as tk
from tkinter import ttk
from persistencia import carregar_dados


class FichasApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Fichas dos Clientes/Pets")
        self.master.geometry("700x500")

        self.clientes = carregar_dados("clientes.json")
        self.agendamentos = carregar_dados("agendamentos.json")

        ttk.Label(master, text="Fichas dos Clientes", font=("Arial", 16)).pack(pady=10)

        frame = ttk.Frame(master)
        frame.pack(pady=5)

        ttk.Label(frame, text="Selecione o Cliente:").grid(row=0, column=0, sticky="e")
        self.cliente_combo = ttk.Combobox(frame, width=40, values=self.listar_clientes())
        self.cliente_combo.grid(row=0, column=1, pady=5)

        ttk.Button(frame, text="Buscar Ficha", command=self.buscar_ficha).grid(row=0, column=2, padx=10)

        self.texto = tk.Text(master, width=85, height=25)
        self.texto.pack(pady=10)

    def listar_clientes(self):
        return [f"{c['nome_cliente']} - {c['nome_pet']}" for c in self.clientes]

    def buscar_ficha(self):
        cliente = self.cliente_combo.get()
        self.texto.delete("1.0", tk.END)

        ficha = [a for a in self.agendamentos if a["cliente"] == cliente]

        if not ficha:
            self.texto.insert(tk.END, "Nenhum registro encontrado para este cliente.")
            return

        for item in ficha:
            linha = f"{item['data']} - {item['servico']} - R$ {item['valor']}\n"
            self.texto.insert(tk.END, linha)
