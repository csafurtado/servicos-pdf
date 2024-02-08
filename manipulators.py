import os
from time import sleep
from PyPDF2 import PdfReader, PdfWriter 
from PIL import Image
import img2pdf

from tkinter import messagebox


class PDFManipulator:
    def __init__(self, path):
        self.path = path
        self.pdf = PdfReader(path)

    # Funções para manipular o PDF escolhido
        
    ## Corta de i até j das páginas de um pdf
    def faz_slice_paginas_pdf(self, limite_inf, limite_sup):
        # Cria o leitor (que recebe o arquivo PDF) e o escritor de arquivo PDF (que irá gerar um novo PDF)            
        nome_arquivo = os.path.basename(self.path).split(".pdf")[0]

        try:
            limite_inf = int(limite_inf) 
            limite_sup = int(limite_sup)

            if limite_inf > limite_sup or limite_inf <= 0 or len(self.pdf.pages) < limite_sup or len(self.pdf.pages) < limite_inf or limite_inf is None or limite_sup is None:
                messagebox.showwarning("ERRO","Verifique se os numeros colocados estão dentro da quantidade de páginas que o PDF possui!")
                return
            writer = PdfWriter()

            with open(f'{nome_arquivo}_{limite_inf}_a_{limite_sup}.pdf', 'wb') as outfile:
                for i in range(limite_inf-1, limite_sup):
                    writer.add_page(self.pdf.pages[i])
                    writer.write(outfile)
            
            sleep(1)

            messagebox.showinfo("SUCESSO","PDF cortado com sucesso!")

        except ValueError:
            messagebox.showwarning("ERRO","Valor dos campos devem ser números e não podem estar vazios!")
            
            return

class ImageManipulator:
    def __init__(self, path):
        self.path = path
        self.img = Image.open(path)

    def transforma_img_em_pdf(self):
        try:
            pdf_da_img = img2pdf.convert(self.img.filename)

            with open(f"{os.path.basename(self.path).split('.')[0]}.pdf", "wb") as arq_pdf:
                arq_pdf.write(pdf_da_img)

            sleep(1)

            messagebox.showinfo("SUCESSO","PDF gerado com sucesso!")

        except:
            messagebox.showwarning("ERRO","Verifique se o caminho da imagem está correto!")

        finally:
            self.img.close()