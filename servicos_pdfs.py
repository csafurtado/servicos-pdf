# Script que executa determinadas funções para PDF
# import pdf2image
import os
from PyPDF2 import PdfFileReader, PdfFileWriter
from tkinter import *
from tkinter import filedialog, messagebox


# Algumas variaveis globais
# poppler_path = r'C:\Users\cristian.csaf\Desktop\RIT\extras'

# Função da janela principal do programa
def abre_janela_principal():
    ## Funções para a janela
    ### Função para abrir janela de escolha de arquivo PDF
    def abrir_arquivo():
        dir_filename =  filedialog.askopenfilename(initialdir=".", title="Escolha o PDF", filetypes=(("PDF files","*.pdf"),("All files", "*.*")))
        label_arq_escolhido["text"] = dir_filename if len(dir_filename) else "Nenhum arquivo escolhido"
    
    # Instancia a janela e a customiza
    j_principal = Tk()
    j_principal.title("Serviços de PDF ao seu dispor")
    j_principal.resizable(width=False, height=False)
    cor_fundo_janela = "#172775"
    j_principal.configure(bg=cor_fundo_janela, takefocus=True, height=300, width=500)
    j_principal.eval('tk::PlaceWindow . center')

    # Coloca os botões das funções na janela e os organiza posicionalmente
    botao_escolher_arquivo = Button(j_principal, command=abrir_arquivo, text="Escolher arquivo", bg=cor_fundo_janela, fg="white")
    botao_slice = Button(j_principal, command= lambda: abre_janela_slice(j_principal, os.path.abspath(label_arq_escolhido["text"])), text="Corte de páginas", height=2, width=14, cursor='dot') #ERRO aqui
    botao_transformar_pdf_em_img = Button(j_principal, text="PDF para JPG", height=2, width=14, cursor="dot")

    botao_escolher_arquivo.place(relx=0.40, rely=0.25)
    botao_slice.place(relx=0.1, rely=0.7)
    botao_transformar_pdf_em_img.place(relx=0.7, rely=0.7)

    # Define textos(labels) a serem mostrados e define sua organização
    label_arq_escolhido = Label(j_principal, text="Nenhum arquivo escolhido", font=('Helvetica 10 bold'), fg="white", bg=cor_fundo_janela)
    label_arq_escolhido.place(relx=.5, rely=.15, anchor=CENTER)
    # label_gambiarra_invisivel =

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
        messagebox.showwarning("ATENCAO", "Escolha um arquivo PDF válido para aplicar alguma função!")
        return

    # Cria janela que tem como pai a janela principal e define suas propriedades
    janela_base = Toplevel(j_principal)     
    janela_base.title("Selecione as páginas")
    janela_base.geometry(f"{300}x{200}+{int((j_principal.winfo_screenwidth()/2)-(300/2))}+{int((j_principal.winfo_screenheight()/2)-(200/2))}")
    janela_base.resizable(False, False)
    cor_fundo_janela = "#383fb8"
    janela_base.configure(bg=cor_fundo_janela, takefocus=True)
    
    # Labels e caixas de entrada
    label_lim_superior = Label(janela_base, text="De:", fg="white", bg=cor_fundo_janela, font=('Helvetica 10 bold'))
    label_lim_inferior = Label(janela_base, text="Até:", fg="white", bg=cor_fundo_janela, font=('Helvetica 10 bold'))
    campo_lim_superior = Entry(janela_base, width=8)
    campo_lim_inferior = Entry(janela_base, width=8)

    label_lim_inferior.place(relx=0.1, rely=0.4)
    label_lim_superior.place(relx=0.1, rely=0.2)
    campo_lim_inferior.place(relx=0.2, rely=0.2)
    campo_lim_superior.place(relx=0.2, rely=0.4)

    # Botão de executar o corte
    botao_executar_slice = Button(janela_base, text="Cortar", width=10, height=5, command= lambda: faz_slice_paginas_pdf(fonte_arq_pdf, campo_lim_inferior.get(), campo_lim_superior.get()))
    botao_executar_slice.place(relx=0.7, rely=0.35)
    # Executa duas funções quando se clica no 'X' desta janela de slice
    # janela_base.protocol('WM_DELETE_WINDOW', func= lambda: faz_bloqueio_janela(1, j_principal))       

    janela_base.mainloop()
    pass


# Funções para manipular o PDF escolhido
## Corta de i até j das páginas de um pdf
def faz_slice_paginas_pdf(fonte_arq_pdf, limite_inf, limite_sup):
    nome_arquivo = os.path.basename(fonte_arq_pdf).split(".pdf")[0]

    try:
        limite_inf = int(limite_inf)
        limite_sup = int(limite_sup)

    except ValueError:
        messagebox.showwarning("ERRO","Valor dos campos devem ser números e não podem estar vazios!")
        return

    finally:
        if limite_inf > limite_sup or limite_inf <= 0:
            messagebox.showwarning("ERRO","Verifique se os numeros colocados estão dentro da quantidade de páginas que o PDF possui!")
            return


        with open(fonte_arq_pdf, 'rb') as infile:
            # Cria o leitor (que recebe o arquivo PDF) e o escritor de arquivo PDF (que irá gerar um novo PDF)
            reader = PdfFileReader(infile)

            if reader.numPages < limite_sup or reader.numPages < limite_inf:
                messagebox.showwarning("ERRO","Verifique se os numeros colocados estão dentro da quantidade de páginas que o PDF possui!")
            writer = PdfFileWriter()

            with open(f'{nome_arquivo}_{limite_inf}_a_{limite_sup}.pdf', 'wb') as outfile:
                for i in range(limite_inf-1, limite_sup):
                    writer.addPage(reader.getPage(i))
                    writer.write(outfile)


def transforma_img_em_pdf(img_fonte):
    pass

# Fluxo principal
def main():

    abre_janela_principal()

    # Escolher qual função executar
    # faz_slice_paginas_pdf(r"C:\Users\cristian.csaf\Desktop\tabela_medicoes_zoch\medicoes_atuais\medicao_57.pdf", 134, 140)


    # CASO TRANSFORMAR IMG EM PDF:
    ## Definir o caminho da imagem desejada e aplicar para transformar em PDF

    pass




if __name__ == "__main__":
    main()


"""
# OBS:

SLICE
-> Para cada erro no corte de páginas, uma janela nova da função é aberta
-> A lógica para verificar erros dentro dos intervalos dados de corte ainda está furada
"""
