from tkinter import *
from tkinter import messagebox, ttk
import requests
import json

# configuração da interface gráfica
UI_COLORS = {
    "darkgray": "#282c34",
    "blue": "dodgerblue",
    "white": "#abb2bf",
    "dimgray": "#5c6370"
}

UI_FONT = ('Helvetica', 14)
UI_FONT_SM = ('Helvetica', 10)  # small

root = Tk()
root.title("Desafio add.")
root["bg"] = UI_COLORS["darkgray"]
root["pady"] = 50
root["padx"] = 50


# customização de widgets do tkinter
class LabelDark(Label):
    def __init__(self, *args, **kwargs):
        Label.__init__(self, *args, **kwargs)
        self["bg"] = UI_COLORS["darkgray"]
        self["fg"] = UI_COLORS["white"]
        self["font"] = UI_FONT_SM
        self["padx"] = 20
        self["pady"] = 20


class ButtonPrimary(Button):
    def __init__(self, *args, **kwargs):
        Button.__init__(self, *args, **kwargs)
        self["bg"] = UI_COLORS["blue"]
        self["fg"] = "white"
        self["font"] = UI_FONT_SM

        # remove bordas
        self["bd"] = 0


class EntryDark(Entry):
    def __init__(self, *args, **kwargs):
        Entry.__init__(self, *args, **kwargs)
        self["bg"] = UI_COLORS["dimgray"]
        self["fg"] = UI_COLORS["white"]
        self["font"] = UI_FONT_SM
        self["bd"] = 0


BASE_URL = "http://localhost:8080/api/v1"


def load_alunos():
    """carrega todos os alunos do banco de dados"""

    try:
        alunos_response = requests.get(BASE_URL + "/alunos")
        alunos_list = alunos_response.json()

        # adiciona formatação
        alunos_list = [f"Nome: {aluno['nome']}, Data de nascimento:{aluno['dataDeNascimento']}" for aluno in alunos_list]

        # limpa o resultado anterior do widget Listbox
        alunos_output.delete(0, END)

        # coloca o novo resultado no widget Listbox
        for aluno in alunos_list:
            alunos_output.insert(END, aluno)

    except requests.exceptions.RequestException as e:
        messagebox.showerror("Não foi possível conectar", "Certifique-se que o servidor está rodando no endereço localhost:8080")
        print(f'Error: {e}')
    

def save_aluno():
    """Adiciona um aluno ao banco de dados"""
    try:
        data = {
            "nome": aluno_name.get(),
            "dataDeNascimento": aluno_birth.get()
        }

        req = requests.post(
            BASE_URL + "/alunos",
            json=data,
            headers={"Content-Type": "application/json"}
            )

        if req.status_code == 200:
            messagebox.showinfo("Pronto", "Cadastro feito com sucesso!")

            # limpa os dados do formulário
            aluno_name.delete(0, END)
            aluno_birth.delete(0, END)

    except requests.exceptions.RequestException as e:
        messagebox.showerror("Não foi possível conectar", "Certifique-se que o servidor está rodando no endereço localhost:8080")
        print(f'Error: {e}')


title = LabelDark(root, text="Cadastrar aluno")
title["font"] = UI_FONT
title.pack()

cadastro_frame = Frame(root, bg=UI_COLORS["darkgray"])
cadastro_frame.pack()

aluno_name = EntryDark(cadastro_frame)
LabelDark(cadastro_frame, text="Nome").grid(row=0, column=0)
aluno_name.grid(row=0, column=1)

aluno_birth = EntryDark(cadastro_frame)
LabelDark(cadastro_frame, text="Data de Nascimento").grid(row=1, column=0)
aluno_birth.grid(row=1, column=1)
ButtonPrimary(root, text="Cadastrar", command=save_aluno).pack()

alunos_output = Listbox(root, width=50, bg=UI_COLORS["dimgray"], fg="white")
alunos_output.pack(pady=30)
ButtonPrimary(root, text="Carregar", command=load_alunos).pack()


if __name__ == "__main__":
    root.mainloop()
