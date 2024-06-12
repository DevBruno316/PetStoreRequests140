import csv #biblioteca que sabe como ler e escrever em um arquivo no formato csv

def read_csv(arquivo_csv):
    dados_csv = [] #cria lista em branco
    try:            #Tentar/tratamento de erro
        with open(arquivo_csv, newline='') as massa:    # COm o arquivo --> Informa o nome e o apelido massa
                                                        #Newline seria o carater do final de linha
            tabela = csv.reader(massa, delimiter=',')   #Coms os dados do arquivo, menos o cabeçalho e informa
                                                        #- que o separador é a vírgula
            next(tabela) # Serve para pular a linha de cabeçalho
            for linha in tabela:
                dados_csv.append(linha) # Guardando os dados separados para uso
        return dados_csv #Devolver os dados para serem usados no teste
    except FileNotFoundError: # Tratamento de erro para aquivo não encontrado
        print(f'Erro: Arquivo não encontrado: {arquivo_csv}')
    except Exception as fail:              # Qualquer erro não previsto
        print(f'Falha imprevista: {fail}') # Mensagem de erro que voltará ao sistema
    

