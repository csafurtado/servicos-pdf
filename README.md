# ServiçosPDF

Cansado de ter que acessar a internet para cortar um PDF ou transformar uma imagem em PDF? O ServiçosPDF pode te ajudar! 

## Requisitos
* É necesário ter o Python 3.12.1 para cima

## Como rodar a aplicação
* Primeiro deve-se criar um ambiente virtual para a execução da aplicação com o comando `python3 -m venv servicosVenv`. Ao finalizar a criação do ambiente virtual, basta entrar nele executando o `servicosVenv\Scripts\activate`.

* Ao concluir o passo anterior, é preciso instalar as bibliotecas necessárias do projeto através do comando `pip install -r requirements.txt`.

* Terminado isso, basta executar a aplicação através do comando `python3 servicos_pdf.py` e ser feliz!

## Utilizando diferentes versões do Python
### WINDOWS:

Caso existam 2 versões diferentes do Python instaladas na máquina, é possível definir "alias" (apelidos) que podem definir cada versão.
Para fazer isso, deve-se seguir os seguintes passos no terminal Powershell:

1. Verificar o resultado do comando `Test-Path $PROFILE`.
    1.1. Se o resultado der False, executar o comando `New-Item -Path $PROFILE -ItemType File -Force`.

2. Abrir um editor de texto podendo ser o notepad mesmo o arquivo $PROFILE através do comando `notepad $PROFILE`.

3. Definir os Alias para as versões de Python instaladas através do comando `Set-Alias python3XX "C:\Users\<nome_do_usuário>\AppData\Local\Programs\Python\Python3XX\python.exe"`, trocando o 3XX (pode ser qualquer nome, mas facilita o entendimento assim) pela versão em questão e colocando o nome do usuário atual.

Com isso agora é possível usar as versões específicas do Python através dos alias dados para cada uma, inclusive para ambientes virtuais criados! Dentro do ambiente não há a necessidade de utilizar estes alias, apenas `python` mesmo, já que o ambiente foi criado já com base na versão certa.


| Modificação | Data |
|----- | ----- |
| Criação do documento | 07/02/2024 |
| Adiciona tópico 'utilizando diferentes versões do Python' | 26/02/2024 |