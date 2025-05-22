import tkinter as tk
from tkinter import ttk, messagebox
from persistencia import carregar_dados, salvar_dados


class FinanceiroApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Controle Financeiro")
        self.master.geometry("600x500")

        self.financeiro = carregar_dados("financeiro.json")

        ttk.Label(master, text="Controle Financeiro", font=("Arial", 16)).pack(pady=10)

        frame = ttk.Frame(master)
        frame.pack(pady=10)

        ttk.Label(frame, text="Descrição:").grid(row=0, column=0, sticky="e")
        self.descricao = ttk.Entry(frame, width=40)
        self.descricao.grid(row=0, column=1, pady=5)

        ttk.Label(frame, text="Valor (R$):").grid(row=1, column=0, sticky="e")
        self.valor = ttk.Entry(frame, width=40)
        self.valor.grid(row=1, column=1, pady=5)

        ttk.Label(frame, text="Tipo:").grid(row=2, column=0, sticky="e")
        self.tipo = ttk.Combobox(frame, values=["Entrada", "Saída"])
        self.tipo.grid(row=2, column=1, pady=5)

        ttk.Button(master, text="Adicionar", command=self.adicionar).pack(pady=10)

        ttk.Label(master, text="Movimentações:").pack()
        self.lista = tk.Listbox(master, width=80, height=10)
        self.lista.pack(pady=10)

        self.saldo_label = ttk.Label(master, text="Saldo Atual: R$ 0.00", font=("Arial", 12, "bold"))
        self.saldo_label.pack(pady=10)

        self.atualizar_lista()

    def adicionar(self):
        try:
            valor = float(self.valor.get())
        except ValueError:
            messagebox.showwarning("Atenção", "Informe um valor numérico.")
            return

        movimento = {
            "descricao": self.descricao.get(),
            "valor": valor,
            "tipo": self.tipo.get()
        }

        if not all([movimento["descricao"], movimento["tipo"]]):
            messagebox.showwarning("Atenção", "Preencha todos os campos.")
            return

        self.financeiro.append(movimento)
        salvar_dados("financeiro.json", self.financeiro)
        messagebox.showinfo("Sucesso", "Movimentação adicionada!")
        self.atualizar_lista()
        self.limpar_campos()

    def atualizar_lista(self):
        self.lista.delete(0, tk.END)
        total_entrada = sum(m["valor"] for m in self.financeiro if m["tipo"] == "Entrada")
        total_saida = sum(m["valor"] for m in self.financeiro if m["tipo"] == "Saída")
        saldo = total_entrada - total_saida

        for m in self.financeiro:
            texto = f"{m['tipo']} - {m['descricao']} - R$ {m['valor']:.2f}"
            self.lista.insert(tk.END, texto)

        self.saldo_label.config(text=f"Saldo Atual: R$ {saldo:.2f}")

    def limpar_campos(self):
        self.descricao.delete(0, tk.END)
        self.valor.delete(0, tk.END)
        self.tipo.set("")
