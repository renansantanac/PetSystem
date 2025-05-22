import tkinter as tk
from tkinter import ttk, messagebox
from persistencia import carregar_dados, salvar_dados


class CadastroApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Cadastro de Clientes/Pets")
        self.master.geometry("600x500")

        self.clientes = carregar_dados("clientes.json")

        ttk.Label(master, text="Cadastro de Cliente/Pet", font=("Arial", 16)).pack(pady=10)

        frame = ttk.Frame(master)
        frame.pack(pady=10)

        # Dados do Cliente
        ttk.Label(frame, text="Nome do Cliente:").grid(row=0, column=0, sticky="e")
        self.nome_cliente = ttk.Entry(frame, width=40)
        self.nome_cliente.grid(row=0, column=1, pady=5)

        ttk.Label(frame, text="Endereço:").grid(row=1, column=0, sticky="e")
        self.endereco = ttk.Entry(frame, width=40)
        self.endereco.grid(row=1, column=1, pady=5)

        ttk.Label(frame, text="Cidade:").grid(row=2, column=0, sticky="e")
        self.cidade = ttk.Entry(frame, width=40)
        self.cidade.grid(row=2, column=1, pady=5)

        # Dados do Pet
        ttk.Label(frame, text="Nome do Pet:").grid(row=3, column=0, sticky="e")
        self.nome_pet = ttk.Entry(frame, width=40)
        self.nome_pet.grid(row=3, column=1, pady=5)

        ttk.Label(frame, text="Espécie:").grid(row=4, column=0, sticky="e")
        self.especie = ttk.Entry(frame, width=40)
        self.especie.grid(row=4, column=1, pady=5)

        ttk.Label(frame, text="Raça:").grid(row=5, column=0, sticky="e")
        self.raca = ttk.Entry(frame, width=40)
        self.raca.grid(row=5, column=1, pady=5)

        ttk.Label(frame, text="Data de Nascimento do Pet (dd/mm/aaaa):").grid(row=6, column=0, sticky="e")
        self.data_nascimento = ttk.Entry(frame, width=40)
        self.data_nascimento.grid(row=6, column=1, pady=5)

        ttk.Button(master, text="Salvar Cadastro", command=self.salvar).pack(pady=10)

        ttk.Label(master, text="Clientes/Pets Cadastrados:", font=("Arial", 12)).pack()
        self.lista = tk.Listbox(master, width=80, height=10)
        self.lista.pack(pady=10)

        self.atualizar_lista()

    def salvar(self):
        cliente = {
            "nome_cliente": self.nome_cliente.get(),
            "endereco": self.endereco.get(),
            "cidade": self.cidade.get(),
            "nome_pet": self.nome_pet.get(),
            "especie": self.especie.get(),
            "raca": self.raca.get(),
            "data_nascimento": self.data_nascimento.get()
        }

        if not all(cliente.values()):
            messagebox.showwarning("Atenção", "Preencha todos os campos.")
            return

        self.clientes.append(cliente)
        salvar_dados("clientes.json", self.clientes)
        messagebox.showinfo("Sucesso", "Cadastro salvo com sucesso!")
        self.atualizar_lista()
        self.limpar_campos()

    def atualizar_lista(self):
        self.lista.delete(0, tk.END)
        for c in self.clientes:
            texto = f"{c['nome_cliente']} - {c['nome_pet']} ({c['especie']} - {c['raca']})"
            self.lista.insert(tk.END, texto)

    def limpar_campos(self):
        self.nome_cliente.delete(0, tk.END)
        self.endereco.delete(0, tk.END)
        self.cidade.delete(0, tk.END)
        self.nome_pet.delete(0, tk.END)
        self.especie.delete(0, tk.END)
        self.raca.delete(0, tk.END)
        self.data_nascimento.delete(0, tk.END)
