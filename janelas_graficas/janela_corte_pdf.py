import os
from models.PDFManipulator import PDFManipulator  # Assumindo que está no mesmo diretório ou é um módulo importável
from tkinter import *
from tkinter import filedialog, messagebox

# Função para abrir arquivo PDF
def abrir_arquivo(label_arq_escolhido, manip_pdf: PDFManipulator):
    dir_filename = filedialog.askopenfilename(initialdir=".", title="Escolha o PDF", filetypes=(("PDF files", "*.pdf"), ("All files", "*.*")))
    if dir_filename:
        label_arq_escolhido.config(text=os.path.basename(dir_filename))
        try: 
            manip_pdf.atribuir_pdf(dir_filename)  # Atualiza o arquivo PDF no manipulador
            num_paginas = len(manip_pdf.pdf.pages)
            label_paginas.config(text=f"Número de páginas: {num_paginas}")
            # Exibe campos de texto e botão de corte
            label_de.grid(row=3, column=0, padx=10, pady=5)
            campo_de.grid(row=3, column=1, padx=10, pady=5)
            label_ate.grid(row=4, column=0, padx=10, pady=5)
            campo_ate.grid(row=4, column=1, padx=10, pady=5)
            botao_cortar.grid(row=5, column=1, padx=10, pady=10)    # mostra o widget após a escolha do arquivo
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao abrir o arquivo PDF: {e}")
    else:
        label_arq_escolhido.config(text="Nenhum arquivo escolhido")

# Função para criar janela de corte de páginas
def inicia_janela_corte(j_principal, manip_pdf: PDFManipulator):
    janela_funcao = Toplevel(j_principal)
    janela_funcao.title("Corte de Páginas")
    janela_funcao.geometry("400x300")
    janela_funcao.config(bg="#383fb8")
    janela_funcao.grab_set()  # Bloqueia a janela principal

    # Texto e botão de seleção de arquivo
    label_arq_escolhido = Label(janela_funcao, text="Nenhum arquivo escolhido", font=('Helvetica', 10, 'bold'), fg="white", bg="#383fb8")
    label_arq_escolhido.grid(row=0, column=0, columnspan=2, pady=20)
    botao_escolher_arquivo = Button(janela_funcao, text="Escolher arquivo", command=lambda: abrir_arquivo(label_arq_escolhido, manip_pdf))
    botao_escolher_arquivo.grid(row=1, column=0, columnspan=2, pady=10)

    global label_paginas, label_de, label_ate, campo_de, campo_ate, botao_cortar
    # Campo para exibir número de páginas
    label_paginas = Label(janela_funcao, text="Número de páginas: 0", font=('Helvetica', 10, 'bold'), fg="white", bg="#383fb8")
    label_paginas.grid(row=2, column=0, columnspan=2, pady=10)

    # Campos para selecionar intervalo de páginas
    label_de = Label(janela_funcao, text="De:", font=('Helvetica', 10), fg="white", bg="#383fb8")
    label_ate = Label(janela_funcao, text="Até:", font=('Helvetica', 10), fg="white", bg="#383fb8")
    campo_de = Entry(janela_funcao, width=5)
    campo_ate = Entry(janela_funcao, width=5)
    botao_cortar = Button(janela_funcao, text="Cortar", command=lambda: cortar_paginas_pdf(manip_pdf))

    # Inicialmente, os widgets não serão exibidos até que um arquivo seja escolhido
    label_de.grid_remove()
    label_ate.grid_remove()
    campo_de.grid_remove()
    campo_ate.grid_remove()
    botao_cortar.grid_remove()

# Função de corte de páginas utilizando a classe PDFManipulator
def cortar_paginas_pdf(manip_pdf: PDFManipulator):
    limite_inf = campo_de.get()
    limite_sup = campo_ate.get()
    if manip_pdf.path:
        manip_pdf.faz_slice_paginas_pdf(manip_pdf.path, limite_inf, limite_sup)
    else:
        messagebox.showwarning("Atenção", "Nenhum arquivo PDF foi selecionado.")