from janelas_graficas.janela_principal import abre_janela_principal
from utils import advices_api

# Início do programa
if __name__ == "__main__":
    frase = advices_api.busca_frase()
    abre_janela_principal(frase)
