import os
from models.PDFManipulator import PDFManipulator  # Assumindo que está no mesmo diretório ou é um módulo importável
from tkinter import *
from tkinter import filedialog, messagebox


# Funções de arrastar e soltar
def finalizar_drag(event):
    # Finaliza o processo de arrastar soltando o item na nova posição
    global item_dragged
    item_dragged = None  # Limpa o item arrastado

def iniciar_drag(event):
    global item_dragged
    # Armazena o índice do item selecionado quando o usuário clica
    widget = event.widget
    index = widget.nearest(event.y)  # Obtém o índice mais próximo da posição do clique
    widget.selection_set(index)  # Seleciona o item clicado

    item_dragged = (index, widget.get(index))  # Salva o índice e o valor do item arrastado

def mover_drag(event):
    global item_dragged
    # Atualiza a posição do item arrastado
    widget = event.widget
    index_atual = widget.nearest(event.y)  # Obtém o índice mais próximo da posição do mouse
    if index_atual != item_dragged[0]:  # Se o item se moveu, reordena a lista
        widget.delete(item_dragged[0])  # Remove o item da posição original
        widget.insert(index_atual, item_dragged[1])  # Insere o item na nova posição
        widget.selection_clear(0, END)  # Limpa a seleção
        widget.selection_set(index_atual)  # Seleciona o item na nova posição

        item_dragged = (index_atual, item_dragged[1])  # Atualiza o índice do item arrastado


# Função para abrir múltiplos arquivos de imagem
def abrir_arquivos(label_arq_escolhido, manip_pdf: PDFManipulator, listbox_arquivos):
    arquivos_escolhidos = filedialog.askopenfilenames(initialdir=".", title="Escolha os arquivos PDF", 
                                            filetypes=(("PDF files", "*.pdf"), ("All files", "*.*")))
    if arquivos_escolhidos:
        listbox_arquivos.delete(0, END)

        for arquivo in arquivos_escolhidos:
            listbox_arquivos.insert(END, arquivo)

        botao_transformar.grid(row=5, column=1, padx=10, pady=10)
    else:
        label_arq_escolhido.config(text="Nenhum arquivo escolhido")

# Função para criar janela de transformação de IMG para PDF com múltiplos arquivos
def inicia_janela_juntar_pdfs(j_principal, manip_pdf: PDFManipulator):
    # Variável global para armazenar o item que está sendo arrastado
    item_dragged = None
    
    janela_funcao = Toplevel(j_principal)
    janela_funcao.title("Juntar arquivos PDFs")
    janela_funcao.geometry("400x400")
    janela_funcao.config(bg="#383fb8")
    janela_funcao.grab_set()  # Bloqueia a janela principal

    # Texto e botão de seleção de arquivos
    label_arq_escolhido = Label(janela_funcao, text="Nenhum arquivo escolhido", font=('Helvetica', 10, 'bold'), fg="white", bg="#383fb8")
    label_arq_escolhido.grid(row=0, column=0, columnspan=2, pady=10)

    # Listbox para exibir os arquivos escolhidos
    listbox_arquivos = Listbox(janela_funcao, width=50, height=10)
    listbox_arquivos.grid(row=1, column=0, columnspan=2, pady=10)

    botao_escolher_arquivos = Button(janela_funcao, text="Escolher arquivos", 
                                     command=lambda: abrir_arquivos(label_arq_escolhido, manip_pdf, listbox_arquivos))
    botao_escolher_arquivos.grid(row=2, column=0, columnspan=2, pady=10)

    global botao_transformar
    botao_transformar = Button(janela_funcao, text="Transformar", command=lambda: juntar_pdfs(listbox_arquivos, manip_pdf))

    # Bind (ligação) dos eventos de mouse aos métodos de drag-and-drop
    listbox_arquivos.bind("<Button-1>", iniciar_drag)  # Quando o botão do mouse é pressionado
    listbox_arquivos.bind("<B1-Motion>", mover_drag)  # Enquanto o mouse está se movendo com o botão pressionado
    listbox_arquivos.bind("<ButtonRelease-1>", finalizar_drag)  # Quando o botão do mouse é solto

    # Inicialmente, o botão de transformar não aparece até que arquivos sejam escolhidos
    botao_transformar.grid_remove()

def juntar_pdfs(listbox_arquivos: Listbox, manip_pdf: PDFManipulator):
    manip_pdf.junta_pdfs(listbox_arquivos.get(0, END))

