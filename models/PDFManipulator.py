import os
from PyPDF2 import PdfReader, PdfWriter
from tkinter import messagebox
from PIL import Image


class PDFManipulator:
    def __init__(self, path=None):
        self.path = path
        self._pdf = None
        self._img = None


    def faz_slice_paginas_pdf(self, fonte_arq_pdf, limite_inf, limite_sup):
        if self._pdf is None:
            return 

        nome_arquivo = os.path.basename(fonte_arq_pdf).split(".pdf")[0]

        try:
            limite_inf = int(limite_inf) 
            limite_sup = int(limite_sup)

            if limite_inf > limite_sup or limite_inf <= 0 or len(self.pdf.pages) < limite_sup or len(self.pdf.pages) < limite_inf:
                messagebox.showwarning("ERRO","Verifique se os numeros colocados estão dentro da quantidade de páginas que o PDF possui!")
                return

        except ValueError:
            messagebox.showwarning("ERRO","Valor dos campos devem ser números e não podem estar vazios!")
            return

        writer = PdfWriter()

        with open(f'{nome_arquivo}_{limite_inf}_a_{limite_sup}.pdf', 'wb') as outfile:
            for i in range(limite_inf-1, limite_sup):
                writer.add_page(self.pdf.pages[i])
            writer.write(outfile)

        messagebox.showinfo("Sucesso", f"Páginas {limite_inf} a {limite_sup} cortadas com sucesso!")

    def junta_pdfs(self, lista_fonte_pdfs : list):
        if lista_fonte_pdfs:  # Verifica se há arquivos no manipulador
            pdf_writer = PdfWriter()

            for pdf in lista_fonte_pdfs:
                pdf_writer.append(pdf)

            pdf_writer.write("resultado_mescla.pdf")
            pdf_writer.close()
            
            messagebox.showinfo("Sucesso", "Pdfs mesclados com sucesso!")
        else:
            messagebox.showwarning("Atenção", "Nenhuma imagem foi selecionada.")


    def transforma_img_para_pdf(self):
        nome_arquivo = os.path.basename(self.path).split(".")[0]

        self.img.convert('RGB').save(f"{nome_arquivo}.pdf")

        messagebox.showinfo("Sucesso", f"Imagem convertida com sucesso!")

    @property
    def pdf(self):
        return PdfReader(self.path) if self.path is not None else None
    
    @property
    def img(self):
        return Image.open(self.path) if self.path is not None else None
    
    def atribuir_pdf(self, path):
        self.path = path
        self._pdf = PdfReader(path)

    def atribuir_img(self, path):
        self.path = path
        self._img = Image.open(path)
