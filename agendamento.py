import tkinter as tk
from tkinter import ttk, messagebox
from persistencia import carregar_dados, salvar_dados
from datetime import datetime


class AgendamentoApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Agendamento de Serviços")
        self.master.geometry("600x400")

        self.clientes = carregar_dados("clientes.json")
        self.agendamentos = carregar_dados("agendamentos.json")

        ttk.Label(master, text="Agendamento de Serviço", font=("Arial", 16)).pack(pady=10)

        frame = ttk.Frame(master)
        frame.pack(pady=10)

        ttk.Label(frame, text="Cliente/Pet:").grid(row=0, column=0, sticky="e")
        self.cliente_combo = ttk.Combobox(frame, width=35, values=self.listar_clientes())
        self.cliente_combo.grid(row=0, column=1, pady=5)

        ttk.Label(frame, text="Serviço:").grid(row=1, column=0, sticky="e")
        self.servico = ttk.Combobox(frame, values=["Banho", "Tosa", "Creche", "Hospedagem"])
        self.servico.grid(row=1, column=1, pady=5)

        ttk.Label(frame, text="Data (dd/mm/aaaa):").grid(row=2, column=0, sticky="e")
        self.data = ttk.Entry(frame)
        self.data.insert(0, datetime.now().strftime("%d/%m/%Y"))
        self.data.grid(row=2, column=1, pady=5)

        ttk.Label(frame, text="Valor (R$):").grid(row=3, column=0, sticky="e")
        self.valor = ttk.Entry(frame)
        self.valor.grid(row=3, column=1, pady=5)

        ttk.Button(master, text="Agendar", command=self.agendar).pack(pady=10)

        ttk.Label(master, text="Agendamentos:").pack()
        self.lista = tk.Listbox(master, width=80, height=10)
        self.lista.pack(pady=10)

        self.atualizar_lista()

    def listar_clientes(self):
        return [f"{c['nome_cliente']} - {c['nome_pet']}" for c in self.clientes]

    def agendar(self):
        agendamento = {
            "cliente": self.cliente_combo.get(),
            "servico": self.servico.get(),
            "data": self.data.get(),
            "valor": self.valor.get()
        }

        if not all(agendamento.values()):
            messagebox.showwarning("Atenção", "Preencha todos os campos.")
            return

        self.agendamentos.append(agendamento)
        salvar_dados("agendamentos.json", self.agendamentos)
        messagebox.showinfo("Sucesso", "Agendamento realizado!")
        self.atualizar_lista()
        self.limpar_campos()

    def atualizar_lista(self):
        self.lista.delete(0, tk.END)
        for a in self.agendamentos:
            texto = f"{a['data']} - {a['cliente']} - {a['servico']} - R$ {a['valor']}"
            self.lista.insert(tk.END, texto)

    def limpar_campos(self):
        self.cliente_combo.set("")
        self.servico.set("")
        self.data.delete(0, tk.END)
        self.data.insert(0, datetime.now().strftime("%d/%m/%Y"))
        self.valor.delete(0, tk.END)
