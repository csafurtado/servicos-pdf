import os
from PDFManipulator import PDFManipulator  # Assumindo que está no mesmo diretório ou é um módulo importável
from tkinter import *
from tkinter import filedialog, messagebox

# Função para abrir arquivo PDF
def abrir_arquivo(label_arq_escolhido, manip_pdf: PDFManipulator):
    dir_filename = filedialog.askopenfilename(initialdir=".", title="Escolha o PDF", filetypes=(("IMG files", ("*.jpg", "*.jpeg", "*.png")), ("All files", "*.*")))
    if dir_filename:
        label_arq_escolhido.config(text=os.path.basename(dir_filename))
        try: 
            manip_pdf.atribuir_img(dir_filename)  # Atualiza o arquivo PDF no manipulador

            botao_transformar.grid(row=5, column=1, padx=10, pady=10)
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao abrir o arquivo de imagem: {e}")
    else:
        label_arq_escolhido.config(text="Nenhum arquivo escolhido")

# Função para criar janela de corte de páginas
def inicia_janela_img_para_pdf(j_principal, manip_pdf: PDFManipulator):
    janela_funcao = Toplevel(j_principal)
    janela_funcao.title("Transformar IMG para PDF")
    janela_funcao.geometry("400x300")
    janela_funcao.config(bg="#383fb8")
    janela_funcao.grab_set()  # Bloqueia a janela principal

    # Texto e botão de seleção de arquivo
    label_arq_escolhido = Label(janela_funcao, text="Nenhum arquivo escolhido", font=('Helvetica', 10, 'bold'), fg="white", bg="#383fb8")
    label_arq_escolhido.grid(row=0, column=0, columnspan=2, pady=20)
    botao_escolher_arquivo = Button(janela_funcao, text="Escolher arquivo", command=lambda: abrir_arquivo(label_arq_escolhido, manip_pdf))
    botao_escolher_arquivo.grid(row=1, column=0, columnspan=2, pady=10)

    global botao_transformar

    botao_transformar = Button(janela_funcao, text="Transformar", command=lambda: transformar_img_pdf(manip_pdf))

    # Inicialmente, os widgets não serão exibidos até que um arquivo seja escolhido
    botao_transformar.grid_remove()

# Função de corte de páginas utilizando a classe PDFManipulator
def transformar_img_pdf(manip_pdf: PDFManipulator):
    if manip_pdf.path:
        manip_pdf.transforma_img_para_pdf()
    else:
        messagebox.showwarning("Atenção", "Nenhum imagem foi selecionada.")