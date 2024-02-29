import os
from time import sleep
import traceback
from PyPDF2 import PdfReader, PdfWriter 
from PIL import Image
import img2pdf

from tkinter import messagebox


class PDFManipulator:
    # Funções para manipular o PDF escolhido

    ## Corta de i até j das páginas de um pdf
    def faz_slice_paginas_pdf(self, path_pdf, limite_inf, limite_sup):
        # Cria o leitor (que recebe o arquivo PDF) e o escritor de arquivo PDF (que irá gerar um novo PDF)            
        nome_arquivo = os.path.basename(path_pdf).split(".pdf")[0]

        try:
            arq_pdf = PdfReader(path_pdf)
            qtd_paginas_arq_pdf = len(arq_pdf.pages)

            limite_inf = int(limite_inf) 
            limite_sup = int(limite_sup)

            if limite_inf >= limite_sup or limite_inf <= 0 or qtd_paginas_arq_pdf < limite_sup or qtd_paginas_arq_pdf < limite_inf or limite_inf is None or limite_sup is None:
                messagebox.showwarning("ERRO","Verifique se os números colocados estão dentro da quantidade de páginas que o PDF possui!")
                return
            
            writer = PdfWriter()


            with open(f'{nome_arquivo}_{limite_inf}_a_{limite_sup}.pdf', 'wb') as outfile:
                for i in range(limite_inf-1, limite_sup):
                    writer.add_page(arq_pdf.pages[i])
                    writer.write(outfile)
            
            sleep(1)

            messagebox.showinfo("SUCESSO","PDF cortado com sucesso!")

        except ValueError:
            messagebox.showwarning("ERRO","Valor dos campos devem ser números e não podem estar vazios!")
            
            return
        
    ## Junta dois Pdfs
    def juntar_pdfs(self, path_pdf1, path_pdf2):
        try:
            arq_pdf1 = PdfReader(path_pdf1)
            arq_pdf2 = PdfReader(path_pdf2)

            nome_arquivo_pdf1 = os.path.basename(path_pdf1).split(".pdf")[0]
            nome_arquivo_pdf2 = os.path.basename(path_pdf2).split(".pdf")[0]

            print(nome_arquivo_pdf1, nome_arquivo_pdf2)

            qtd_paginas_pdf1 = self.retorna_qtd_paginas_pdf(path_pdf1)
            qtd_paginas_pdf2 = self.retorna_qtd_paginas_pdf(path_pdf2)

            writer = PdfWriter()

            with open(f"{nome_arquivo_pdf1}_e_{nome_arquivo_pdf2}.pdf", 'wb') as outfile:
                for i in range(0, qtd_paginas_pdf1+qtd_paginas_pdf2):
                    if i < qtd_paginas_pdf1:
                        writer.add_page(arq_pdf1.pages[i])
                        writer.write(outfile)
                    
                    else:
                        writer.add_page(arq_pdf2.pages[i-qtd_paginas_pdf1])
                        writer.write(outfile)

            sleep(1)

            messagebox.showinfo("SUCESSO","PDF cortado com sucesso!")            

        except:
            messagebox.showwarning("ERRO","Erro encontrado ao juntar PDFs! Verifique o caminho dos PDFs escolhidos!")
            traceback.print_exc()
            return

    def retorna_qtd_paginas_pdf(self, path_pdf):
        try:
            arq_pdf = PdfReader(path_pdf)

            return len(arq_pdf.pages)

        except:
            messagebox.showwarning("ERRO","Erro encontrado ao verificar a qtd de páginas do PDF!")


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