import os
from tkinter import *
from janela_grafica_corte_PDF import inicia_janela_corte
from janela_grafica_img_pdf import inicia_janela_img_para_pdf
from PDFManipulator import PDFManipulator  # Assumindo que está no mesmo diretório ou é um módulo importável


# Função da janela principal
def abre_janela_principal():
    j_principal = Tk()
    j_principal.title("Manipulação de PDFs")
    j_principal.geometry("500x400")
    j_principal.config(bg="#172775")

    manip_pdf = PDFManipulator()  # Criação do objeto de manipulação de PDF

    # Botões na janela principal
    botao_corte = Button(j_principal, text="Cortar Páginas", command=lambda: inicia_janela_corte(j_principal, manip_pdf))
    botao_corte.grid(row=1, column=0, padx=20, pady=20)

    botao_pdf_img = Button(j_principal, text="Imagem para PDF", command=lambda: inicia_janela_img_para_pdf(j_principal, manip_pdf))
    botao_pdf_img.grid(row=1, column=1, padx=20, pady=20)

    j_principal.mainloop()