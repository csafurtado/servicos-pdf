# Script que executa determinadas funções para PDF
# import pdf2image
import os
from tkinter import *
from tkinter import filedialog, messagebox

from manipulators import PDFManipulator, ImageManipulator

## Funções para a janela
### Função para abrir janela de escolha de arquivo PDF
def abrir_arquivo(label_item):
    dir_filename = filedialog.askopenfilename(initialdir=".", title="Escolha o PDF", filetypes=(("PDF files","*.pdf"),("Image Files",["*.jpg","*.jpeg","*.png"]),("All files", "*.*")))
    label_item["text"] = dir_filename if len(dir_filename) else "Nenhum arquivo escolhido"

# Função da janela principal do programa
def abre_janela_principal():
    # Instancia a janela e a customiza
    j_principal = Tk()
    j_principal.title("Serviços de PDF ao seu dispor")
    j_principal.resizable(True, True)
    cor_fundo_janela = "#172775"
    j_principal.configure(bg=cor_fundo_janela, takefocus=True, height=300, width=500)
    j_principal.eval('tk::PlaceWindow . center')

    # Define textos(labels) a serem mostrados e define sua organização
    label_arq_escolhido = Label(j_principal, text="Nenhum arquivo escolhido", font=('Helvetica 10 bold'), fg="white", bg=cor_fundo_janela)
    label_arq_escolhido.place(relx=.5, rely=.15, anchor=CENTER)

    # Coloca os botões das funções na janela e os organiza posicionalmente
    botao_escolher_arquivo = Button(j_principal, command= lambda: abrir_arquivo(label_arq_escolhido), text="Escolher arquivo", bg=cor_fundo_janela, fg="white")
    botao_slice = Button(j_principal, command= lambda: abre_janela_slice(j_principal, os.path.abspath(label_arq_escolhido["text"])), text="Cortar PDF", height=2, width=14, cursor='dot')
    botao_transformar_pdf_em_img = Button(j_principal, command= lambda: abrir_janela_transforma_img_em_pdf(os.path.abspath(label_arq_escolhido["text"])), text="JPG para PDF", height=2, width=14, cursor="dot")
    botao_juntar_pdfs = Button(j_principal, command= lambda: abrir_janela_juntar_pdfs(j_principal), text="Juntar PDFs", height=2, width=14, cursor="dot")
    
    botao_escolher_arquivo.place(relx=0.5, rely=0.25, anchor=CENTER)
    botao_slice.place(relx=0.1, rely=0.7, anchor="w")
    botao_transformar_pdf_em_img.place(relx=0.9, rely=0.7, anchor="e")
    botao_juntar_pdfs.place(relx=0.5, rely=0.7, anchor=CENTER)

    j_principal.mainloop()

# Bloqueia ou desbloqueia janela em questao (pensar em implementar dps)
def faz_bloqueio_janela(estado, janela):
    if estado:
        for item in janela.winfo_children():
            item.configure(state='active')
    else:
        for item in janela.winfo_children():
            item.configure(state='disable')

# Mostra janela de aviso de saída da função caso o botão "X" da janela principal seja clicado
def janela_saida(janela_principal):
    if messagebox.askyesno("AVISO", "Deseja sair do programa?"):
        janela_principal.destroy()
        exit(1)

def abre_janela_slice(j_principal, fonte_arq_pdf):   
    # Bloqueia os widgets da janela principal, permitindo
    # faz_bloqueio_janela(0, j_principal)
    if os.path.basename(fonte_arq_pdf) == "Nenhum arquivo escolhido" or fonte_arq_pdf.split(".")[-1] != "pdf":
        messagebox.showwarning("ATENCAO", "Escolha um arquivo PDF válido!")
        return
    
    manipuladorPDF = PDFManipulator()

    # Cria janela que tem como pai a janela principal e define suas propriedades
    janela_base = Toplevel(j_principal)     
    janela_base.title("Selecione as páginas")
    janela_base.geometry(f"{300}x{200}+{int((j_principal.winfo_screenwidth()/2)-(300/2))}+{int((j_principal.winfo_screenheight()/2)-(200/2))}")
    janela_base.resizable(False, False)
    cor_fundo_janela = "#383fb8"
    janela_base.configure(bg=cor_fundo_janela, takefocus=True)
    janela_base.grab_set()
    
    # Labels e caixas de entrada
    label_lim_superior = Label(janela_base, text="De:", fg="white", bg=cor_fundo_janela, font=('Helvetica 10 bold'))
    label_lim_inferior = Label(janela_base, text="Até:", fg="white", bg=cor_fundo_janela, font=('Helvetica 10 bold'))
    campo_lim_superior = Entry(janela_base, width=8)
    campo_lim_inferior = Entry(janela_base, width=8)

    label_qtd_paginas_pdf = Label(janela_base, text=f"Quantidade de páginas: {manipuladorPDF.retorna_qtd_paginas_pdf(fonte_arq_pdf)}", fg="white", bg=cor_fundo_janela, font=('Helvetica 10 bold'))
    label_qtd_paginas_pdf.place(relx=0.1, rely=0.8)

    label_lim_inferior.place(relx=0.1, rely=0.4)
    label_lim_superior.place(relx=0.1, rely=0.2)
    campo_lim_inferior.place(relx=0.2, rely=0.2)
    campo_lim_superior.place(relx=0.2, rely=0.4)

    # Botão de executar o corte
    botao_executar_slice = Button(janela_base, background="#cf5f5f", text="Cortar", width=10, height=3, command= lambda: manipuladorPDF.faz_slice_paginas_pdf(fonte_arq_pdf, campo_lim_inferior.get(), campo_lim_superior.get()))
    botao_executar_slice.place(relx=0.7, rely=0.35)
    # Executa duas funções quando se clica no 'X' desta janela de slice
    # janela_base.protocol('WM_DELETE_WINDOW', func= lambda: faz_bloqueio_janela(1, j_principal))       

    janela_base.mainloop()
    pass

def abrir_janela_transforma_img_em_pdf(fonte_img):
    # Bloqueia os widgets da janela principal, permitindo
    # faz_bloqueio_janela(0, j_principal)

    if os.path.basename(fonte_img) == "Nenhum arquivo escolhido" or fonte_img.split(".")[-1] not in ["jpg", "jpeg", "png"]:
        messagebox.showwarning("ATENCAO", "Escolha um arquivo de imagem válido!")
        return
    
    manipuladorImagem = ImageManipulator(fonte_img)
    manipuladorImagem.transforma_img_em_pdf()

def abrir_janela_juntar_pdfs(j_principal):
    manipuladorPDF = PDFManipulator()

    # Cria janela que tem como pai a janela principal e define suas propriedades
    janela_base = Toplevel(j_principal)     
    janela_base.title("Selecione os arquivos PDFs para juntar")
    janela_base.geometry(f"{400}x{300}+{int((j_principal.winfo_screenwidth()/2)-(300/2))}+{int((j_principal.winfo_screenheight()/2)-(200/2))}")
    janela_base.resizable(False, False)
    cor_fundo_janela = "#383fb8"
    janela_base.configure(bg=cor_fundo_janela, takefocus=True)
    janela_base.grab_set()

    # Define textos(labels) a serem mostrados e define sua organização

    # Labels e caixas de entrada
    label_pdf1 = Label(janela_base, text="PDF 1", fg="white", bg=cor_fundo_janela, font=('Helvetica 10 bold'))
    label_pdf2 = Label(janela_base, text="PDF 2", fg="white", bg=cor_fundo_janela, font=('Helvetica 10 bold'))
    botao_escolher_pdf1 = Button(janela_base, command=lambda: abrir_arquivo(label_pdf1), text="Escolher arquivo", bg=cor_fundo_janela, fg="white")
    botao_escolher_pdf2 = Button(janela_base, command=lambda: abrir_arquivo(label_pdf2), text="Escolher arquivo", bg=cor_fundo_janela, fg="white")

    label_pdf1.place(relx=0.5, rely=0.15, anchor=CENTER)
    botao_escolher_pdf1.place(relx=0.5, rely=0.3, anchor=CENTER)
    label_pdf2.place(relx=0.5, rely=0.5, anchor=CENTER)
    botao_escolher_pdf2.place(relx=0.5, rely=0.65, anchor=CENTER)

    # Botão de executar o corte
    botao_juntar = Button(janela_base, background="#f3e56b", text="Juntar", width=15, height=1, command= lambda: manipuladorPDF.juntar_pdfs(label_pdf1['text'], label_pdf2['text']))
    botao_juntar.place(relx=0.5, rely=0.85, anchor=CENTER)

    janela_base.mainloop() 
